.PHONY: help up down run-server run-bot test cq

help:
	@echo "all commands:"
	@echo "up (run docker compose)"
	@echo "down (stop docker compose)"
	@echo "run-server (run fastapi app)"
	@echo "run-bot (run discord bot)"
	@echo "test (run pytest)"
	@echo "cq (run pre-commit)"

up:
	docker compose up -d

down:
	docker compose down

run-server:
	uv sync
	uv run alembic upgrade head
	uv run uvicorn src.backend.app.api.main:app --host 0.0.0.0 --port 8000

run-bot:
	uv sync
	uv run python -m src.backend.app.bot.main

test:
	uv sync
	uv run pytest

cq:
	uv sync
	uv run pre-commit run --all-files
