import json

with open("app/data/faults.json", "r", encoding="utf-8") as file:
    faults = json.load(file)

def find_fault(faults, fault_code):
    fault_code = fault_code.upper()
    return faults.get(fault_code)

def get_all_faults():
    return faults
        
def print_fault(fault_code, fault_data):
    if fault_data is None:
        print("Ошибка не найдена")
        return

    print(f"\nКод ошибки: {fault_code} - {fault_data.get('name_en', 'Название ошибки не указано')}")
    print(f"Название: {fault_data.get('name_ru', 'Название отсутствует')}")
    print(f"Описание: {fault_data.get('description', 'Описание отсутствует')}")

    print("Что проверить:")
    checks = fault_data.get('check', 'Проверки отсутствуют')

    for check in checks:
        print(f"- {check}")
        
    print("Что сделать:")
    actions = fault_data.get('action', 'Действия отсутствуют')

    for action in actions:
        print(f"- {action}")

def print_all_faults(faults):
    if not faults:
        print("Список ошибок пуст")
        return
    
    for fault_code, fault_data in faults.items():
        print_fault(fault_code, fault_data)
        print("-" * 40)