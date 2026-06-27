def _format_bullet_list(items, empty_text):
    if not items:
        return f"• {empty_text}"

    return "\n".join(f"• {item}" for item in items)


def format_fault_not_found(fault_code):
    code = fault_code.strip().upper() or "без кода"

    return (
        f"❌ Ошибка {code} не найдена.\n\n"
        "Проверь код и попробуй ещё раз.\n"
        "Пример: F005"
    )


def format_fault(fault_code, fault_data):
    code = fault_code.strip().upper()

    if fault_data is None:
        return format_fault_not_found(code)

    name_en = fault_data.get("name_en") or "Название ошибки не указано"
    name_ru = fault_data.get("name_ru") or "Название отсутствует"
    description = fault_data.get("description") or "Описание отсутствует"

    checks = fault_data.get("check") or []
    actions = fault_data.get("action") or []

    checks_text = _format_bullet_list(checks, "Проверки отсутствуют")
    actions_text = _format_bullet_list(actions, "Действия отсутствуют")

    return (
        f"⚠️ Ошибка {code} — {name_en}\n\n"
        f"📌 Название:\n"
        f"{name_ru}\n\n"
        f"📝 Описание:\n"
        f"{description}\n\n"
        f"🔎 Что проверить:\n"
        f"{checks_text}\n\n"
        f"🛠 Что сделать:\n"
        f"{actions_text}"
    )


def format_all_faults(faults):
    if not faults:
        return "Список ошибок пуст"

    result = []

    for fault_code, fault_data in faults.items():
        result.append(format_fault(fault_code, fault_data))

    return "\n\n━━━━━━━━━━━━━━━━━━━━\n\n".join(result)