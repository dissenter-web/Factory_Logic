def format_spare_part_not_found(part_name):
    name = part_name.strip() or ""

    return (
        f"❌ Запчасть {name} не найдена.\n\n"
        "Проверьте название и попробуйте ещё раз.\n"
    )

def format_spare_part(part_name, parts_data):
    name = part_name.strip()

    if parts_data is None:
        return format_spare_part_not_found(name)
    for i in parts_data:
        return (
             "\n\n━━━━━━━━━━━━━━━━━━━━\n"
            f"\n🏷️ Название: {i["name"]}\n\n"
            f"🔢 SAP: {i["sap"]}\n\n"
            f"📦 Место хранения: {i["location"]}\n\n"
             "\n━━━━━━━━━━━━━━━━━━━━\n\n"
        )
