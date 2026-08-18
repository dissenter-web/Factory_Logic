from app.interfaces.max_bot.button import Button
from app.interfaces.max_bot.screen import Screen


def make_vfd_menu_screen(
    vfd_catalog: dict,
) -> Screen:
    buttons = []

    for manufacturer_id, manufacturer_data in (
        vfd_catalog.items()
    ):
        buttons.append(
            Button(
                text=f"• {manufacturer_data['name']}",
                payload=(
                    f"vfd_manufacturer:"
                    f"{manufacturer_id}"
                ),
            )
        )

    buttons.append(
        Button(
            text="🏠 Главное меню",
            payload="main_menu",
        )
    )

    return Screen(
        title="vfd_menu",
        text=(
            "⚡ Частотные приводы\n\n"
            "Выберите производителя оборудования.\n\n"
            "Доступные производители:"
        ),
        buttons=buttons,
    )


def make_model_menu_screen(
    manufacturer_id: str,
    manufacturer_data: dict,
) -> Screen:
    buttons = []

    for model_id, model_data in manufacturer_data["models"].items():
        buttons.append(
            Button(
                text=f"• {model_data['name']}",
                payload=(
                    f"vfd_select:"
                    f"{manufacturer_id}:"
                    f"{model_id}"
                ),
            )
        )

    buttons.append(
        Button(
            text="⬅ Назад",
            payload="vfd_menu",
        )
    )

    buttons.append(
        Button(
            text="🏠 Главное меню",
            payload="main_menu",
        )
    )

    return Screen(
        title="vfd_models",
        text=(
            f"{manufacturer_data['name']}\n\n"
            "Доступные модели приводов:"
        ),
        buttons=buttons,
    )


def make_vfd_actions_screen(
    manufacturer_id: str,
    manufacturer_data: dict,
    model_data: dict,
) -> Screen:
    return Screen(
        title="vfd_actions",
        text=(
            f"{manufacturer_data['name']} "
            f"{model_data['name']}\n\n"
            "Выберите действие:"
        ),
        buttons=[
            Button(
                text="🔍 Поиск ошибки",
                payload="vfd_fault_search",
            ),
            Button(
                text="⚙️ Параметры быстрого запуска",
                payload="vfd_parameters",
            ),
            Button(
                text="⬅ Назад",
                payload=(
                    f"vfd_manufacturer:"
                    f"{manufacturer_id}"
                ),
            ),
            Button(
                text="🏠 Главное меню",
                payload="main_menu",
            ),
        ],
    )


def make_fault_input_screen(
    model_data: dict,
) -> Screen:
    return Screen(
        title="vfd_fault_input",
        text=(
            f"🔍 Поиск ошибки {model_data['name']}\n\n"
            "Введите код ошибки.\n"
            f"Например: {model_data['fault_example']}"
        ),
        buttons=[
            Button(
                text="⬅ Назад",
                payload="vfd_current",
            ),
            Button(
                text="🏠 Главное меню",
                payload="main_menu",
            ),
        ],
    )