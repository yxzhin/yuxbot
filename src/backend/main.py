from .infra.utils import StructuredLogger


def main() -> None:
    """Точка входа для запуска приложения. biscuits."""
    StructuredLogger.setup()
    # //@TODO
    # bot = create_bot()
    # bot.run(Config.BOT_TOKEN)


if __name__ == "__main__":
    main()
