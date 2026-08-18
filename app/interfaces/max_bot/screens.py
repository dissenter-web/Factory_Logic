from app.interfaces.max_bot.screen import Screen
from app.interfaces.max_bot.button import Button
from app.interfaces.max_bot.vfd_catalog import VFD_CATALOG
from app.interfaces.max_bot.vfd_screens import (
    make_vfd_menu_screen,
)


START_SCREEN = Screen(
    title="start",
    text=(
          "⚙️ Factory Logic\n\n"
          "Справочник для инженеров группы по ремонту электрооборудования.\n\n"
          "Система помогает быстро находить:\n"
          "• ошибки и параметры частотных приводов;\n"
          #"• техническую документацию;\n"
          #"• стандартные рабочие процедуры;\n"
          "• информацию по запасным частям.\n\n"
          "👇 Выберите нужный раздел.\n\n"
            ),
    buttons=[
        Button(text="⚡ Частотные приводы", payload="vfd_menu"),
        Button(text="📦 Запчасти", payload="spare_parts_menu"),
        Button(text="ℹ️ О проекте", payload="about_project"),
    ],
)

FALLBACK_SCREEN = Screen(
    title="fallback_main_menu",
    text=(
        "❌ Запрошенный раздел не найден.\n\n"
        "Вернитесь в главное меню."
    ),
    buttons=[
        Button(text="🏠 Главное меню", payload="main_menu"),
    ],
)

MAIN_SCREEN = Screen(
    title="main_menu",
    text=(
        "🏠 Главное меню\n\n"
        "Выберите рабочий раздел:\n\n"
        "⚡ Частотные приводы\n"
        "Ошибки и параметры "
        "по преобразователям частоты.\n\n"
        "📦 Запчасти\n"
        "Поиск запасных частей по названию\n\n"
        "ℹ️ О проекте\n"
        "Версия системы и служебная информация."
    ),
    buttons=[
        Button(text="⚡ Частотные приводы", payload="vfd_menu"),
        Button(text="📦 Запчасти", payload="spare_parts_menu"),
        Button(text="ℹ️ О проекте", payload="about_project"),
    ],
)

VFD_SCREEN = make_vfd_menu_screen(
    vfd_catalog=VFD_CATALOG,
)

SPARE_PARTS_SCREEN = Screen(
    title="spare_parts_menu",
    text=(
        "Это демонстрационный раздел без привязки к реальному складу запчастей.\n\n"
        "📦 Меню поиска запчастей.\n\n"
        "Выберите оборудование:\n"
    ),
    buttons=[
        Button(text="• Bodymaker", payload="bodymaker"),
        Button(text="🏠 Главное меню", payload="main_menu"),
    ],
)

BODYMAKER_SPARE_PART_INPUT_SCREEN = Screen(
    title="bodymaker_spare_part_input",
    text=(
        "🔍 Поиск запчастей Bodymaker\n\n"
        "Введите название запчасти или его часть.\n"
        "Например: датчик"
    ),
    buttons=[
        Button(
            text="⬅ Назад",
            payload="spare_parts_menu",
        ),
        Button(
            text="🏠 Главное меню",
            payload="main_menu",
        ),
    ],
)

ABOUT_PROJECT = Screen(
    title="about_project",
    text=(
          "ℹ️ О проекте\n\n"
          "Factory Logic\n\n"
          "Справочник для инженеров группы по ремонту электрооборудования.\n\n"
          "Версия: 0.2.0-alpha\n"
          "Статус: В активной разработке\n\n"
          "Разработчик: Dissenter\n\n"
          "Сайт:\n"
          "https://dissenter.top\n\n"
          "© 2026 Factory Logic"
            ),
    buttons=[
        Button(text="Назад", payload="main_menu"),
    ],
)

SCREENS = {
    "main_menu": MAIN_SCREEN,
    "vfd_menu": VFD_SCREEN,
    "spare_parts_menu": SPARE_PARTS_SCREEN,
    "bodymaker_spare_part_input": BODYMAKER_SPARE_PART_INPUT_SCREEN,
    "about_project": ABOUT_PROJECT,
    }