def format_spare_part_not_found(part_name):
    name = part_name.strip() or ""

    return (
        f"❌ Запчасть {name} не найдена.\n\n"
        "Проверьте название и попробуйте ещё раз.\n"
    )

def format_spare_part(part_name, parts_data):
    name = part_name.strip()
    format_list = []

    if not parts_data or not part_name:
        return format_spare_part_not_found(name)
    for i in parts_data:
          format_list.append(
                            "\n\n━━━━━━━━━━━━━━━━━━━━\n"
                            f"\n🏷️ Название: {i["name"]}\n\n"
                            f"🔢 SAP: {i["sap"]}\n\n"
                            f"📦 Место хранения: {i["location"]}\n\n"
                            "\n━━━━━━━━━━━━━━━━━━━━\n\n"
                        )
    return format_list