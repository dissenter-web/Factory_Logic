def render_screen(screen):
    buttons = []

    for button in screen.buttons:
        buttons.append(
            [
                {
                    "type": "callback",
                    "text": button.text,
                    "payload": button.payload,
                }
            ]
        )

    return {
        "text": screen.text,
        "attachments": [
            {
                "type": "inline_keyboard",
                "payload": {
                    "buttons": buttons,
                },
            }
        ],
    }