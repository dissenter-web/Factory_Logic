import json

with open("faults.json", "r", encoding="utf-8") as file:
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

while True:
    print("\n1. Показать ошибки")
    print("2. Найти ошибку")
    print("3. Выход\n")

    choice = input("Выберите действие: ")

    if choice == "1":
        all_faults = get_all_faults()
        print_all_faults(all_faults)

    elif choice == "2":
        fault_code = input("Введите код ошибки: ")
        fault_data = find_fault(faults, fault_code)
        print_fault(fault_code, fault_data)

    elif choice == "3":
        break

    else:
        print("Неизвестная команда")   