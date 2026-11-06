
from app.interfaces.max_bot.renderer import render_screen
from app.repositories.json_repository import load_pinout_image


class Polling:
    def __init__(self, client, handler):
        self.client = client
        self.handler = handler
        self.marker = None

    def poll_once(self):
        data = self.client.get_updates(self.marker)

        for update in data["updates"]:
            screen = self.handler.handle_update(update)

            if screen is None:
                continue

            update_type = update.get("update_type")

            if update_type == "bot_started":
                chat_id = update["chat_id"]
                message = render_screen(screen)
                self.client.send_message(chat_id, message)

            elif update_type == "message_callback":
                callback = update["callback"]
                callback_id = callback["callback_id"]
                payload = callback.get("payload", "")

                if payload in ("pinout_rj45", "pinout_m12"):
                    connector = payload.removeprefix("pinout_")

                    image_bytes = load_pinout_image(connector)
                    upload_result = self.client.upload_image(image_bytes)

                    image_token = upload_result.get("token")

                    if image_token is None:
                        photos = upload_result.get("photos", {})
                        image_token = next(
                            iter(photos.values()), {}
                        ).get("token")

                    if image_token is None:
                        raise ValueError(
                            "MAX не вернул токен изображения"
                        )

                    message = render_screen(
                        screen,
                        image_token=image_token,
                    )

                    self.client.answer_callback(
                        callback_id,
                        message,
                    )

                else:
                    message = render_screen(screen)
                    self.client.answer_callback(
                        callback_id,
                        message,
                    )

            elif update_type == "message_created":
                chat_id = update["message"]["recipient"]["chat_id"]
                message = render_screen(screen)
                self.client.send_message(chat_id, message)

        self.marker = data["marker"]
