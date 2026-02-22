from collections.abc import AsyncGenerator
from typing import Any

import pytest
from sqlalchemy import event
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.backend.services.clans.infra.models import *
from src.backend.services.clans.infra.repositories.sqlal import (
    SqlAlchemyClanMemberRepository,
    SqlAlchemyClanRepository,
)
from src.backend.services.clans.infra.units_of_work.sqlal import (
    SqlAlchemyClanUnitOfWork,
)
from src.backend.services.players.infra.models import *
from src.backend.shared.infra.events import InMemoryEventBus
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

            def restart_savepoint(sess, trans):
                if (
                    trans.nested
                    and not getattr(trans, "_parent", None)
                    or not trans._parent
                ):
                    sess.begin_nested()

            event.listen(
                session.sync_session, "after_transaction_end", restart_savepoint
            )

            try:
                yield session
            finally:
                event.remove(
                    session.sync_session, "after_transaction_end", restart_savepoint
                )

        await transaction.rollback()


@pytest.fixture
def event_bus():
    return InMemoryEventBus()


@pytest.fixture
async def clan_member_repo_factory(db_sess):
    return lambda: SqlAlchemyClanMemberRepository(db_sess)


@pytest.fixture
async def clan_repo_factory(db_sess):
    return lambda: SqlAlchemyClanRepository(db_sess)


@pytest.fixture
async def clan_uow_factory(db_sess):
    return lambda: SqlAlchemyClanUnitOfWork(db_sess)
