class Polling:
    def __init__(self, client, handler):
        self.client = client
        self.handler = handler
        self.marker = None

    def poll_once(self):
        data = self.client.get_updates(self.marker)

        for update in data["updates"]:
            self.handler.handle_update(update)

        self.marker = data["marker"]

        

        screen = self.handler.handle_update(update)

        if screen is not None:
            print(screen.text)