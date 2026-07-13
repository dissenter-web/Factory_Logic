class Navigator:
    def __init__(self, screens, fallback_screen):
        self.screens = screens
        self.fallback_screen = fallback_screen

    def get_screen(self, payload):
        return self.screens.get(payload, self.fallback_screen)