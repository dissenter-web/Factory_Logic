class Handler:
    def __init__(self, navigator, start_screen):
        self.navigator = navigator
        self.start_screen = start_screen

    def handle_update(self, update):
        update_type = update.get("update_type")

        if update_type == "bot_started":
            return self.start_screen

        if update_type == "message_callback":
            payload = update["callback"]["payload"]
            return self.navigator.get_screen(payload)

        return None