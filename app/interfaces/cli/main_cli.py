from app.interfaces.cli.router import SCREENS


def run_cli():
    current_screen = "main"

    while current_screen != "exit":
        screen_func = SCREENS[current_screen]
        current_screen = screen_func()