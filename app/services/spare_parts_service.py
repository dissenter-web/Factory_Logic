def normalize_spare_parts(spare_part: str) -> str:
    return spare_part.strip().lower()


def find_spare_part(list_spare_parts: dict, spare_part: str) -> list[dict]:
    query = normalize_spare_parts(spare_part)

    if not query:
        return []

    found_spare_parts = []

    for part_data in list_spare_parts.values():
        name = part_data.get("name", "").lower()

        if query in name:
            found_spare_parts.append(part_data)

    return found_spare_parts