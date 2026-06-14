import json

with open("faults.json", "r", encoding="utf-8") as file:
    faults = json.load(file)

def find_fault(code):
    return faults.get(code)

def show_faults():
    for fault_code, fault_data in faults.items():
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

while True:
    print("\n1. Показать ошибки")
    print("2. Найти ошибку")
    print("3. Выход\n")

    choice = input("Выберите действие: ")

    if choice == "1":
        show_faults()

    elif choice == "2":
        code = input("Введите код ошибки: ").upper()
        description = find_fault(code)

        if description:
            print(f"Ошибка найдена. Название: {description}")
        else:
            print("Ошибка не найдена.")

    elif choice == "3":
        break

    else:
        print("Неизвестная команда")   