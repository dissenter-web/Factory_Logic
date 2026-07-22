import os

from dotenv import load_dotenv


load_dotenv()


def get_required_env(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise RuntimeError(
            f"Обязательная переменная окружения {name} не задана"
        )

    return value


MAX_BOT_TOKEN = get_required_env("MAX_BOT_TOKEN")