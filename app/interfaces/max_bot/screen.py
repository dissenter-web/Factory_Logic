from dataclasses import dataclass
from pathlib import Path
from app.interfaces.max_bot.button import Button

@dataclass
class Screen:
    title: str
    text: str
    buttons: list[Button]
    image_path: Path | None = None