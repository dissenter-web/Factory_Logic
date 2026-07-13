class Handler:
    def __init__(self, navigator):
        self.navigator = navigator
        
    def handle_payload(self, payload):
        return self.navigator.get_screen(payload)
    
    def handle_update(self, update):
        update_type = update.get("update_type")

        if update_type != "message_callback":
            return None

        payload = update["callback"]["payload"]

        return self.navigator.get_screen(payload)