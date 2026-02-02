import os

from .infra.utils import ConfigLoader

ConfigLoader.import_env()


class Config:
    """
    Конфигурационные параметры приложения, загружаемые из переменных окружения.
    Атрибуты доступны напрямую, без создания экземпляра класса.
    """

    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    BOT_SECRET = os.getenv("BOT_SECRET", "")
    BOT_CLIENT_ID = int(os.getenv("BOT_CLIENT_ID", 0))
    BOT_OWNER_ID = int(os.getenv("BOT_OWNER_ID", 0))
    BOT_STATUS_MESSAGE = os.getenv("BOT_STATUS_MESSAGE", "")
    BOT_COGS = os.getenv("BOT_COGS", "").strip().split(",")

    API_URL = os.getenv("API_URL", "")

    DATABASE_USERNAME = os.getenv("DATABASE_USERNAME", "admin")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "admin")
    DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_PORT = int(os.getenv("DATABASE_PORT", 5432))
    DATABASE_NAME = os.getenv("DATABASE_NAME", "app")
    DATABASE_URL = (
        f"postgresql+asyncpg://{DATABASE_USERNAME}:{DATABASE_PASSWORD}"
        f"@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    )

    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

    APP_NAME = os.getenv("APP_NAME", "")
    APP_DESCRIPTION = os.getenv("APP_DESCRIPTION", "")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
    ENABLE_API_DOCS = os.getenv("ENABLE_API_DOCS", "true").lower() == "true"
