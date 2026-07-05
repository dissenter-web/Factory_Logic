def format_spare_part_not_found(part_name: str) -> str:
    name = part_name.strip() or "без названия"

    return (
        f"❌ Запчасть {name} не найдена.\n\n"
        "Проверьте название и попробуйте ещё раз."
    )


def format_spare_part(part_name: str, parts_data: list[dict]) -> str:
    if not parts_data:
        return format_spare_part_not_found(part_name)

    result = []

    for part in parts_data:
        result.append(
            "\n━━━━━━━━━━━━━━━━━━━━\n"
            f"\n🏷️ Название: {part.get('name', 'Не указано')}\n"
            f"🔢 SAP: {part.get('sap', 'Не указан')}\n"
            f"📦 Место хранения: {part.get('location', 'Не указано')}\n"
            "\n━━━━━━━━━━━━━━━━━━━━"
        )

    return "\n".join(result)