import requests


class BotClient:
    def __init__(self, token):
        self.base_url = "https://platform-api2.max.ru"
        self.headers = {
            "Authorization": token,
            "Content-Type": "application/json",
        }

    def get_updates(self, marker=None):
        params = {}

        if marker is not None:
            params["marker"] = marker

        response = requests.get(
            f"{self.base_url}/updates",
            headers=self.headers,
            params=params,
            timeout=35,
        )

        response.raise_for_status()

        return response.json()
    
    def send_message(self, chat_id, message):
        response = requests.post(
            f"{self.base_url}/messages",
            headers=self.headers,
            params={"chat_id": chat_id},
            json=message,
            timeout=10,
        )

        response.raise_for_status()
        return response.json()
    
    def answer_callback(self, callback_id, message):
        response = requests.post(
            f"{self.base_url}/answers",
            headers=self.headers,
            params={"callback_id": callback_id},
            json={"message": message},
            timeout=10,
        )

        response.raise_for_status()
        return response.json()