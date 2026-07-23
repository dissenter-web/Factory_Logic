def format_parameters(parameters_data: dict) -> str:
    title = parameters_data.get(
        "title",
        "Параметры быстрого запуска",
    )

    sections = parameters_data.get("sections") or []
    notes = parameters_data.get("notes") or []

    result = [f"⚙️ {title}"]

    for section in sections:
        section_title = section.get("title", "Раздел")
        parameters = section.get("parameters") or []

        result.append(f"\n📌 {section_title}")

        for parameter in parameters:
            code = parameter.get("code", "Код не указан")
            name = parameter.get("name", "Название не указано")
            value = parameter.get("value", "Значение не указано")

            result.append(
                f"\n{code} — {name}\n"
                f"{value}"
            )

    if notes:
        result.append("\n⚠️ Примечания")

        for note in notes:
            result.append(f"• {note}")

    return "\n".join(result)