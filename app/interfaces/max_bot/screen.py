from dataclasses import dataclass
from app.interfaces.max_bot.button import Button

@dataclass
class Screen:
    title: str
    text: str
    buttons: list[Button]