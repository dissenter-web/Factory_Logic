from app.interfaces.max_bot.navigator import Navigator
from app.interfaces.max_bot.handler import Handler
from app.interfaces.max_bot.polling import Polling
from app.interfaces.max_bot.screens import SCREENS, FALLBACK_SCREEN
from app.interfaces.max_bot.client import BotClient
from app.config import MAX_BOT_TOKEN

client = BotClient(MAX_BOT_TOKEN)

navigator = Navigator(SCREENS, FALLBACK_SCREEN)

handler = Handler(navigator)

polling = Polling(client, handler)

polling.poll_once()