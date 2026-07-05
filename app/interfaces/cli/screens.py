from app.repositories import json_repository
from app.interfaces.cli.actions import (
    find_fault_action,
    get_all_faults_action,
    find_spare_part_action,
)

#Главный экран
def main_screen():
    print("\n1. Приводы")
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
    print("\n1. Allen_Bradley")
    print("2. ABB")
    print("3. SEW_Eurodrive")
    print("0. Назад\n")
    print("--------------------")

    choice = input("Выберите действие: ")

    if choice == "1":
        return "ab_menu"

    if choice == "2":
        return "abb_menu"
    
    if choice == "3":
        return "sew_menu"

    if choice == "0":
        return "main"

    return "vfd_main"

#Экран приводов Allen Bradley
def ab_menu_screen():
    manufacturer = "allen_bradley"
    print("\n1. PF525")
    print("2. PF40")
    print("3. PF753")
    print("4. PF160")
    print("0. Назад\n")
    print("--------------------")

    choice = input("Выберите модель VFD: ")
    
    if choice == "1":
        model_vfd_ab_screen("pf525", manufacturer)

    if choice == "2":
        model_vfd_ab_screen("pf40", manufacturer)
    
    if choice == "3":
        model_vfd_ab_screen("pf753", manufacturer)
    
    if choice == "4":
        model_vfd_ab_screen("pf160", manufacturer)

    if choice == "0":
        return "vfd_main"

    return "ab_menu"

#Экран моделей приводов Allen Bradley
def model_vfd_ab_screen(model, manufacturer):
    
    print("\n1. Показать все ошибки")
    print("2. Найти ошибку по коду")
    print("3. Назад\n")

    choice = input("Выберите действие: ")

    if choice == "1":
        all_fault_vfd_screen(manufacturer, model)

    if choice == "2":
        search_fault_vfd_screen(manufacturer, model)

    if choice == "0":
        return "ab_menu"
  
    return "model_vfd_ab"

#Экран поиска ошибок привода
def search_fault_vfd_screen(manufacturer, model):
    data_type = "faults"
    list_faults = json_repository.load_vfd_data(manufacturer, model, data_type)

    fault_code = (input("Введите код ошибки: "))

    find_fault_action(list_faults, fault_code)

    input("Нажмите Enter для возврата...")
    return "model_vfd_ab"

#Экран вывода всех ошибок привода
def all_fault_vfd_screen(manufacturer, model):
    data_type = "faults"
    list_faults = json_repository.load_vfd_data(manufacturer, model, data_type)

    get_all_faults_action(list_faults)

    input("Нажмите Enter для возврата...")
    return "model_vfd_ab"

#Экран запчастей
def spare_parts_screen():
    print("\n1. Бодимейкер")
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