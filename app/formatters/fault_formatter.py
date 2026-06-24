def format_fault(fault_code, fault_data):
    if fault_data is None:
        return "Ошибка не найдена"
        
    result = []

    result.append(f"\nКод ошибки: {fault_code} - {fault_data.get('name_en', 'Название ошибки не указано')}")
    result.append(f"Название: {fault_data.get('name_ru', 'Название отсутствует')}")
    result.append(f"Описание: {fault_data.get('description', 'Описание отсутствует')}")

    result.append("Что проверить:")
    checks = fault_data.get('check', [])
    if checks:
        for check in checks:
            result.append(f"- {check}")
    else:
        result.append('- Проверки отсутствуют')

    result.append("Что сделать:")
    actions = fault_data.get('action', [])
    if actions:
        for action in actions:
            result.append(f"- {action}")
    else:
        result.append('- Действия отсутствуют')

    return "\n".join(result)

def format_all_faults(faults):
    if not faults:
        return "Список ошибок пуст"
    
    result = []
    
    for fault_code, fault_data in faults.items():
        result.append(format_fault(fault_code, fault_data))
        result.append("-" * 40)

    return "\n".join(result)