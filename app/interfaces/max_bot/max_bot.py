import time
import requests
from app.config import MAX_BOT_TOKEN

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



if __name__ == "__main__":
    print(request_api("GET", "/updates"))