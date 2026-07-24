from app.interfaces.max_bot.screen import Screen
from app.interfaces.max_bot.button import Button


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

VFD_SCREEN = Screen(
    title="vfd_menu",
    text=(
        "⚡ Частотные приводы\n\n"
        "Выберите производителя оборудования.\n\n"
        "Доступные производители:\n"
    ),
    buttons=[
        Button(text="• Allen-Bradley", payload="ab_menu"),
        Button(text="• ABB", payload="abb_menu"),
        Button(text="• SEW-EURODRIVE", payload="sew_menu"),
        Button(text="• Control Techniques", payload="ct_menu"),
        Button(text="• HPMont", payload="hpmont_menu"),
        Button(text="🏠 Главное меню", payload="main_menu"),
    ],
)

#Экраны AllenBradley
AB_MENU_SCREEN = Screen(
    title="ab_menu",
    text=(
        "Allen-Bradley\n\n"
        "Доступные модели приводов:\n"
    ),
    buttons=[
        Button(text="PF-525", payload="ab_pf525"),
        Button(text="⬅ Назад", payload="vfd_menu"),
        Button(text="🏠 Главное меню", payload="main_menu"),
    ],
)

#Экраны AllenBradley PowerFlex 525
AB_PF525_SCREEN = Screen(
    title="ab_pf525",
    text=(
        "PowerFlex 525\n\n"
        "Выберите действие:\n"
    ),
    buttons=[
        Button(text="🔍 Поиск ошибки", payload="pf_525_fault_search"),
        Button(text="📋 Все ошибки", payload="pf_525_faults"),
        Button(text="⚙️ Параметры", payload="pf_525_parameters"),
        Button(text="⬅ Назад", payload="ab_menu"),
        Button(text="🏠 Главное меню", payload="main_menu"),
    ],
)

PF_525_FAULT_INPUT_SCREEN = Screen(
    title="pf_525_fault_input",
    text=(
        "🔍 Поиск ошибки PowerFlex 525\n\n"
        "Введите код ошибки.\n"
        "Например: F005"
    ),
    buttons=[
        Button(text="⬅ Назад", payload="ab_pf525"),
        Button(text="🏠 Главное меню", payload="main_menu"),
    ],
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
          "GitHub:\n"
          "https://github.com/dissenter-web\n\n"
          "© 2026 Factory Logic"
            ),
    buttons=[
        Button(text="Назад", payload="main_menu"),
    ],
)

SCREENS = {
    "main_menu": MAIN_SCREEN,
    "vfd_menu": VFD_SCREEN,
    "ab_menu": AB_MENU_SCREEN,
    "ab_pf525": AB_PF525_SCREEN,
    "pf_525_fault_input": PF_525_FAULT_INPUT_SCREEN,
    "spare_parts_menu": SPARE_PARTS_SCREEN,
    "bodymaker_spare_part_input": BODYMAKER_SPARE_PART_INPUT_SCREEN,
    "about_project": ABOUT_PROJECT,
    }