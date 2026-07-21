from app.interfaces.max_bot.renderer import render_screen


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

            if update.get("update_type") == "bot_started":
                chat_id = update["chat_id"]
                message = render_screen(screen)
                self.client.send_message(chat_id, message)

            elif update.get("update_type") == "message_callback":
                callback_id = update["callback"]["callback_id"]
                message = render_screen(screen)
                self.client.answer_callback(callback_id, message)

        self.marker = data["marker"]