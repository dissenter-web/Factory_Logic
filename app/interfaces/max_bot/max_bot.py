import time
import requests
from app.config import MAX_BOT_TOKEN
from app.services import faults_service
from app.formatters.fault_formatter import format_fault, format_all_faults
from app.repositories.json_repository import load_faults

API_URL = "https://platform-api.max.ru"

HEADERS = {
    "Authorization": MAX_BOT_TOKEN,
    "Content-Type": "application/json",
}


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
                
def faults_handling():
    faults = load_faults()

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