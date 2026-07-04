import time
import requests
from app.config import MAX_BOT_TOKEN
from app.services import faults_service, spare_parts_service
from app.formatters.fault_formatter import format_fault, format_all_faults
from app.formatters.spare_parts_formatter import format_spare_part
from app.repositories.json_repository import load_vfd_data, load_spare_parts_data

API_URL = "https://platform-api.max.ru"

HEADERS = {
    "Authorization": MAX_BOT_TOKEN,
    "Content-Type": "application/json",
}

manufacturer = "allen_bradley"
model = "pf525"
data_type = "faults"

def request_api(method, path, params=None, json=None):
    response = requests.request(
        method=method,
        url=f"{API_URL}{path}",
        headers=HEADERS,
        params=params,
        json=json,
        timeout=35,
    )

    if response.status_code >= 400:
        print("API ERROR:", response.status_code)
        print(response.text)
        return None

    if response.text:
        return response.json()

    return {}

def echo():
    marker = None

    while True:
        data = request_api(
            "GET", 
            "/updates",
            params={"marker": marker} if marker else None,
            )
        
        marker = data["marker"]

        updates = data["updates"]

        if updates:
            message = updates[0]["message"]
            is_bot = message["sender"]["is_bot"]

            if not is_bot:
                message_text = message["body"]["text"]
                chat_id = message["recipient"]["chat_id"]
        
                request_api(
                        "POST",
                        "/messages",
                        params={"chat_id": chat_id},
                        json={"text": message_text}
                    )
                
def send_start_menu(chat_id):
    request_api(
        "POST",
        "/messages",
        params={"chat_id": chat_id},
        json={
            "text": (
                "⚙️ FactoryLogic\n\n"
                "Cправочник для инженеров группы по ремонту электрооборудования.\n\n"
                "Здесь можно быстро найти ошибки VFD,\n"
                "параметры, инструкции, стандартные \n"
                "рабочие процедуры.\n\n"
                "👇 Выберите нужный раздел.\n\n"
                "💻 *Разделы VFD, СРП и номера ЗИП находятся в стадии разработки.\n"
                "Поиск ошибок пока доступен только по Allen Bradley - PF525. Для тестирования бота введите код ошибки, например f005."
            ),
            "attachments": [
                {
                    "type": "inline_keyboard",
                    "payload": {
                        "buttons": [
                            [
                                {
                                    "type": "callback",
                                    "text": "⚡ VFD",
                                    "payload": "vfd_menu"
                                },
                                {
                                    "type": "callback",
                                    "text": "📜 СРП",
                                    "payload": "srp_menu"
                                }
                            ],
                            [
                                {
                                    "type": "callback",
                                    "text": "🛠️ Номера ЗИП",
                                    "payload": "zip_menu"
                                },
                                {
                                    "type": "callback",
                                    "text": "ℹ️ О проекте",
                                    "payload": "about_project"
                                }
                            ]
                        ]
                    }
                }
            ]
        }
    )
                
def faults_handling():
    faults = load_vfd_data(manufacturer, model, data_type)

    marker = None

    while True:
        data = request_api(
            "GET", 
            "/updates",
            params={"marker": marker} if marker else None,
            )
        
        marker = data["marker"]

        updates = data["updates"]

        if updates:
            update = updates[0]

            update_type = update["update_type"]

            if update_type == "bot_started":
                chat_id = update["chat_id"]
                send_start_menu(chat_id)
                continue

            if "message" not in update:
                continue

            message = update["message"]
            is_bot = message["sender"]["is_bot"]

            if not is_bot:
                message_text = message["body"]["text"]
                chat_id = message["recipient"]["chat_id"]

                fault_code = faults_service.normalize_fault_code(message_text)
                fault_data = faults_service.find_fault(faults, fault_code)
        
                request_api(
                        "POST",
                        "/messages",
                        params={"chat_id": chat_id},
                        json={"text": format_fault(fault_code.upper(), fault_data)}
                    )


if __name__ == "__main__":
    faults_handling()