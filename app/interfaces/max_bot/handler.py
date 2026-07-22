from app.services.faults_service import find_fault
from app.formatters.fault_formatter import format_fault
from app.interfaces.max_bot.screen import Screen
from app.interfaces.max_bot.button import Button

class Handler:
    def __init__(self, navigator, start_screen, user_state, faults):
        self.navigator = navigator
        self.start_screen = start_screen
        self.user_state = user_state
        self.faults = faults

    def handle_update(self, update):
        update_type = update.get("update_type")

        if update_type == "bot_started":
            return self.start_screen

        if update_type == "message_callback":
            payload = update["callback"]["payload"]

            if payload == "pf_525_fault_search":
                user_id = update["callback"]["user"]["user_id"]

                self.user_state.set(
                    user_id,
                    {
                        "action": "fault_search",
                        "manufacturer": "allen_bradley",
                        "model": "pf_525",
                    },
                )

                return self.navigator.get_screen("pf_525_fault_input")

            return self.navigator.get_screen(payload)
        
        if update_type == "message_created":
            user_id = update["message"]["sender"]["user_id"]
            text = update["message"]["body"]["text"]

            state = self.user_state.get(user_id)

            if state is None:
                return None

            if state["action"] == "fault_search":
                fault = find_fault(self.faults, text)
                message = format_fault(text, fault)

                self.user_state.clear(user_id)

                return Screen(
                    title="fault_result",
                    text=message,
                    buttons=[
                        Button(
                            text="🔍 Искать другую ошибку",
                            payload="pf_525_fault_search",
                        ),
                        Button(
                            text="⬅ Назад",
                            payload="ab_pf525",
                        ),
                        Button(
                            text="🏠 Главное меню",
                            payload="main_menu",
                        ),
                    ],
                )

            return None

        return None