from app.repositories import json_repository
from app.interfaces.cli.actions import (
    find_fault_action,
    get_all_faults_action,
    find_spare_part_action,
)

#Главный экран
def main_screen():
    print("\n=== Factory Logic ===")
    print("1. Частотные приводы")
    print("2. Запчасти")
    print("0. Выход")
    print("--------------------")

    choice = input("Выберите действие: ")

    if choice == "1":
        return "vfd_main"

    if choice == "2":
        return "spare_parts_menu"

    if choice == "0":
        return "exit"

    return "main"

#Главный экран приводов
def vfd_main_screen():
    print("\n=== Частотные приводы ===")
    print("1. Allen-Bradley")
    print("2. ABB")
    print("3. SEW Eurodrive")
    print("0. Назад")
    print("--------------------")

    choice = input("Выберите производителя: ")

    if choice == "1":
        return "ab_menu"

    if choice == "2":
        print("Раздел ABB пока в разработке")
        input("Enter для возврата...")
        return "vfd_main"

    if choice == "3":
        print("Раздел SEW пока в разработке")
        input("Enter для возврата...")
        return "vfd_main"

    if choice == "0":
        return "main"

    return "vfd_main"

#Экран приводов Allen Bradley
def ab_menu_screen():
    print("\n=== Allen-Bradley ===")
    print("1. PowerFlex 525")
    print("2. PowerFlex 40")
    print("3. PowerFlex 753")
    print("4. PowerFlex 160")
    print("0. Назад")
    print("--------------------")

    choice = input("Выберите модель: ")

    if choice == "1":
        return "ab_pf525_menu"

    if choice == "2":
        return "ab_pf40_menu"

    if choice == "3":
        return "ab_pf753_menu"

    if choice == "4":
        return "ab_pf160_menu"

    if choice == "0":
        return "vfd_main"

    return "ab_menu"

#Обертка под модели приводов Allen Bradley
AB_MANUFACTURER = "allen_bradley"


def ab_pf525_screen():
    return model_vfd_ab_screen("pf525", "ab_pf525_menu")


def ab_pf40_screen():
    return model_vfd_ab_screen("pf40", "ab_pf40_menu")


def ab_pf753_screen():
    return model_vfd_ab_screen("pf753", "ab_pf753_menu")


def ab_pf160_screen():
    return model_vfd_ab_screen("pf160", "ab_pf160_menu")

#Общий  экран моделей приводов Allen Bradley
def model_vfd_ab_screen(model: str, current_screen: str):
    print(f"\n=== Allen-Bradley {model.upper()} ===")
    print("1. Показать все ошибки")
    print("2. Найти ошибку по коду")
    print("0. Назад")
    print("--------------------")

    choice = input("Выберите действие: ")

    if choice == "1":
        all_fault_vfd_screen(AB_MANUFACTURER, model)
        print("--------------------")
        input("Нажмите Enter для возврата...")
        return current_screen

    if choice == "2":
        search_fault_vfd_screen(AB_MANUFACTURER, model)
        print("--------------------")
        input("Нажмите Enter для возврата...")
        return current_screen

    if choice == "0":
        return "ab_menu"

    return current_screen

#Экран поиска ошибок привода
def search_fault_vfd_screen(manufacturer, model):
    data_type = "faults"
    list_faults = json_repository.load_vfd_data(manufacturer, model, data_type)

    fault_code = (input("Введите код ошибки: "))

    return find_fault_action(list_faults, fault_code)

#Экран вывода всех ошибок привода
def all_fault_vfd_screen(manufacturer, model):
    data_type = "faults"
    list_faults = json_repository.load_vfd_data(manufacturer, model, data_type)

    return get_all_faults_action(list_faults)

#Экран запчастей
def spare_parts_screen():
    print("\n=== Запчасти ===")
    print("1. Поиск запчастей - Бодимейкер")
    print("0. Назад")
    print("--------------------")

    choice = input("Выберите машину: ")

    if choice == "1":
        return "search_spare_parts_bm"

    if choice == "0":
        return "main"

    return "spare_parts_menu"

#Экран поиска запчастей Бодимейкера
def search_spare_parts_bm_screen():
    data_type = "bm"
    list_spare_parts = json_repository.load_spare_parts_data(data_type)
    spare_part = input("Введите название запчасти: ")

    find_spare_part_action(spare_part, list_spare_parts)

    input("Нажмите Enter для возврата...")
    return "spare_parts_menu"