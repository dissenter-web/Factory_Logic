import json

with open("faults.json", "r", encoding="utf-8") as file:
    faults = json.load(file)

def find_fault(code):
    return faults.get(code)

def show_faults():
    for code, description in faults.items():
        print(f"{code} - {description}")

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