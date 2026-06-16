import time
import requests


TOKEN = "f9LHodD0cOJ674VwsfSwrD-vIYytZ2nSC-z__7kz2AjedCunVne9PGJUAuADEiCvzzKyvsO-KRRtbECe1BsX"

API_URL = "https://platform-api.max.ru"

HEADERS = {
    "Authorization": TOKEN,
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


def get_updates(marker=None):
    params = {
        "limit": 10,
        "timeout": 30,
    }

    if marker:
        params["marker"] = marker

    return request_api(
        method="GET",
        path="/updates",
        params=params,
    )


def make_keyboard():
    return [
        {
            "type": "inline_keyboard",
            "payload": {
                "buttons": [
                    [
                        {
                            "type": "callback",
                            "text": "⚡ Частотники",
                            "payload": "button_drives",
                        }
                    ],
                    [
                        {
                            "type": "callback",
                            "text": "📋 СОП",
                            "payload": "button_sop",
                        }
                    ],
                ]
            },
        }
    ]


def send_message(user_id, text):
    body = {
        "text": text,
        "attachments": make_keyboard(),
    }

    return request_api(
        method="POST",
        path="/messages",
        params={"user_id": user_id},
        json=body,
    )


def answer_callback(callback_id, text):
    body = {
        "message": {
            "text": text,
            "attachments": make_keyboard(),
        },
        "notification": "Кнопка нажата",
    }

    return request_api(
        method="POST",
        path="/answers",
        params={"callback_id": callback_id},
        json=body,
    )


def get_user_id_from_message(update):
    message = update.get("message", {})
    sender = message.get("sender", {})
    return sender.get("user_id")


def get_text_from_message(update):
    message = update.get("message", {})
    body = message.get("body", {})
    return body.get("text", "")


def handle_message(update):
    user_id = get_user_id_from_message(update)
    text = get_text_from_message(update)

    if not user_id:
        print("Не нашёл user_id в сообщении:")
        print(update)
        return

    print(f"Сообщение от {user_id}: {text}")

    send_message(
        user_id=user_id,
        text=(
            f"Эхо: {text}\n\n"
            "Связь с ботом работает.\n"
            "Ниже две тестовые кнопки."
        ),
    )


def handle_callback(update):
    callback = update.get("callback", {})

    callback_id = callback.get("callback_id")
    payload = callback.get("payload")

    print("Нажата кнопка:", payload)

    if payload == "button_drives":
        answer_callback(
            callback_id=callback_id,
            text=(
                "Ты нажал кнопку: ⚡ Частотники\n\n"
                "Позже здесь будет:\n"
                "Allen Bradley → PowerFlex 525 → Ошибки / Параметры"
            ),
        )
        return

    if payload == "button_sop":
        answer_callback(
            callback_id=callback_id,
            text=(
                "Ты нажал кнопку: 📋 СОП\n\n"
                "Позже здесь будут стандартные рабочие процедуры."
            ),
        )
        return

    answer_callback(
        callback_id=callback_id,
        text=f"Неизвестная кнопка: {payload}",
    )


def handle_bot_started(update):
    user = update.get("user", {})
    user_id = user.get("user_id")

    if not user_id:
        print("Не нашёл user_id в событии старта:")
        print(update)
        return

    send_message(
        user_id=user_id,
        text=(
            "Бот запущен.\n\n"
            "Это тестовое меню.\n"
            "Напиши любое сообщение или нажми кнопку."
        ),
    )


def handle_update(update):
    update_type = update.get("update_type") or update.get("type")

    print("\nUPDATE:", update_type)

    if update_type == "message_created":
        handle_message(update)
        return

    if update_type == "message_callback":
        handle_callback(update)
        return

    if update_type in ("bot_started", "user_added"):
        handle_bot_started(update)
        return

    print("Необработанное событие:")
    print(update)


def main():
    marker = None

    print("Бот запущен.")
    print("Остановить: Ctrl + C")

    while True:
        data = get_updates(marker)

        if data is None:
            time.sleep(3)
            continue

        updates = data.get("updates", [])
        marker = data.get("marker", marker)

        for update in updates:
            handle_update(update)


if __name__ == "__main__":
    main()