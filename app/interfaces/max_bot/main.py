from app.interfaces.max_bot.navigator import Navigator
from app.interfaces.max_bot.handler import Handler
from app.interfaces.max_bot.polling import Polling
from app.interfaces.max_bot.screens import SCREENS, FALLBACK_SCREEN, START_SCREEN
from app.interfaces.max_bot.client import BotClient
from app.interfaces.max_bot.user_state import UserState
from app.config import MAX_BOT_TOKEN
from app.repositories import json_repository


def main():
    client = BotClient(MAX_BOT_TOKEN)

    navigator = Navigator(SCREENS, FALLBACK_SCREEN)

    user_state = UserState()
    
    pf525_faults = json_repository.load_vfd_data(
    manufacturer="allen_bradley",
    model="pf525",
    data_type="faults",
    )
    
    handler = Handler(
        navigator=navigator,
        start_screen=START_SCREEN,
        user_state=user_state,
        faults=pf525_faults,
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