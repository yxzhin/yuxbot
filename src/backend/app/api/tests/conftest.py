from collections.abc import AsyncGenerator, Callable
from typing import Any

import pytest
from dishka import AsyncContainer, make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient
from sqlalchemy import event
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.backend.app.api.di.providers import (
    DBSessionProvider,
    EventBusProvider,
    UnitOfWorkFactoryProvider,
    UseCaseProvider,
)
from src.backend.app.api.v1.routers import clans_router, players_router
from src.backend.shared.utils import Base


@pytest.fixture
async def test_engine() -> AsyncGenerator[AsyncEngine, Any]:
    """Создает асинхронный движок базы данных для тестов."""
    engine = create_async_engine(
        "sqlite+aiosqlite:///:memory:",
        future=True,
    )

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield engine
    await engine.dispose()


@pytest.fixture
async def db_sess(test_engine: AsyncEngine) -> AsyncGenerator[AsyncSession, Any]:
    """Создает новую сессию и откатывает все изменения после теста."""
    async with test_engine.connect() as conn:
        transaction = await conn.begin()

        sessionmaker = async_sessionmaker(
            bind=conn,
            expire_on_commit=False,
            class_=AsyncSession,
        )

        async with sessionmaker() as session:
            await session.begin_nested()

            @event.listens_for(session.sync_session, "after_transaction_end")
            def restart_savepoint(sess, trans):
                if trans.nested and not trans._parent.nested:
                    sess.begin_nested()

            yield session

        await transaction.rollback()


@pytest.fixture
async def app_container(
    db_sess: AsyncSession,
) -> AsyncGenerator[AsyncContainer, Any]:
    app_container = make_async_container(
        DBSessionProvider(db_sess),
        EventBusProvider(),
        UnitOfWorkFactoryProvider(),
        UseCaseProvider(),
    )
    yield app_container
    await app_container.close()


@pytest.fixture
def app(app_container: AsyncContainer) -> FastAPI:
    """Создает FastAPI приложение для тестирования."""
    app = FastAPI()
    app.include_router(clans_router)
    app.include_router(players_router)

    setup_dishka(container=app_container, app=app)
    return app


@pytest.fixture
async def httpx_client(app: FastAPI) -> AsyncGenerator[AsyncClient, Any]:
    """Создает HTTP-клиент для тестирования API."""

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as ac:
        yield ac


@pytest.fixture
def create_player(httpx_client: AsyncClient) -> Callable[[int, str], Any]:
    """
    Фикстура для создания пользователя через API.
    Возвращает функцию, которая создает пользователя с заданными параметрами.
    """

    async def _create_player(
        player_id: int,
        username: str,
    ) -> dict:
        payload = {
            "player_id": player_id,
            "username": username,
        }

        response = await httpx_client.post("/players/create", json=payload)
        assert response.status_code == 201, response.text

        json = response.json()
        assert json["success"] is True

        return json["player"]

    return _create_player


@pytest.fixture
def create_clan(httpx_client: AsyncClient) -> Callable[[str, str, int], Any]:
    """
    Фикстура для создания клана через API.
    Возвращает функцию, которая создает клан с заданными параметрами.
    """

    async def _create_clan(clan_name: str, clan_tag: str, owner_id: int) -> dict:
        payload = {
            "clan_name": clan_name,
            "clan_tag": clan_tag,
            "owner_id": owner_id,
        }

        response = await httpx_client.post("/clans/create", json=payload)
        assert response.status_code == 201, response.text

        json = response.json()
        assert json["success"] is True

        return json["clan"]

    return _create_clan
