def render_screen(screen, image_token=None):
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

    attachments = [
    {
        "type": "inline_keyboard",
        "payload": {
            "buttons": buttons,
        },
    }
]

    if image_token is not None:
        attachments.append(
            {
                "type": "image",
                "payload": {
                    "token": image_token,
                },
            }
        )

    return {
        "text": screen.text,
        "attachments": attachments,
    }