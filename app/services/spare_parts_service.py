def normalize_spare_parts(spare_part):
    return spare_part.strip().upper()

def find_spare_part(list_spare_parts, spare_part):
    spare_part = normalize_spare_parts(spare_part)
    return list_spare_parts.get(spare_part)