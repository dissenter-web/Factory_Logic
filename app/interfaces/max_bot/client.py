import requests

class BotClient:
    def __init__(self, token):
        self.base_url = "https://platform-api2.max.ru"
        self.headers = {
            "Authorization": token,
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