from app.interfaces.max_bot.screen import Screen
from app.interfaces.max_bot.button import Button

MAIN_SCREEN = Screen(
    title="main_menu",
    text="Главное меню Factory Logic",
    buttons=[
        Button(text="Частотные привода", payload="vfd_menu"),
        Button(text="Запчасти", payload="spare_parts_menu"),
        Button(text="О проекте", payload="about_project"),
    ],
)

FALLBACK_SCREEN = Screen(
    title="fallback_main_menu",
    text="Раздел не найден.\nВозврат в главное меню Factory Logic",
    buttons=[
        Button(text="Частотные привода", payload="vfd_menu"),
        Button(text="Запчасти", payload="spare_parts_menu"),
        Button(text="О проекте", payload="about_project"),
    ],
)

SCREENS = {
    "main_menu": MAIN_SCREEN,
    }