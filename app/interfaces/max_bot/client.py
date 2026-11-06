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

    def get_image_upload_url(self):
        response = requests.post(
            f"{self.base_url}/uploads",
            headers=self.headers,
            params={"type": "image"},
            timeout=10,
        )

        response.raise_for_status()

        return response.json()["url"]

    def upload_image(self, image_bytes: bytes):
        upload_url = self.get_image_upload_url()

        response = requests.post(
            upload_url,
            files={
                "data": ("pinout.png", image_bytes, "image/png")
            },
            timeout=30,
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