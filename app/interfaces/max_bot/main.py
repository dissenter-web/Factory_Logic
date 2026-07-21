from app.interfaces.max_bot.navigator import Navigator
from app.interfaces.max_bot.handler import Handler
from app.interfaces.max_bot.polling import Polling
from app.interfaces.max_bot.screens import SCREENS, FALLBACK_SCREEN, START_SCREEN
from app.interfaces.max_bot.client import BotClient
from app.config import MAX_BOT_TOKEN


def main():
    client = BotClient(MAX_BOT_TOKEN)

    navigator = Navigator(SCREENS, FALLBACK_SCREEN)

    handler = Handler(
        navigator=navigator,
        start_screen=START_SCREEN,
    )

    polling = Polling(
        client,
        handler
    )

    try:
        while True:
            polling.poll_once()
    except KeyboardInterrupt:
        print("Polling остановлен")

if __name__ == "__main__":
    main()