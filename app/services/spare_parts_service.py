def normalize_spare_parts(spare_part):
    return spare_part.strip().lower()

def find_spare_part(list_spare_parts, spare_part):
    found_spare_parts = []
    spare_part = normalize_spare_parts(spare_part)

    for x in list_spare_parts:
        if spare_part in list_spare_parts[x]["name"].lower():
            found_spare_parts.append(list_spare_parts[x])

    return found_spare_parts