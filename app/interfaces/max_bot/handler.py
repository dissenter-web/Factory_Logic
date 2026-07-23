from app.services.faults_service import find_fault
from app.formatters.fault_formatter import format_fault
from app.formatters.parameters_formatter import format_parameters
from app.services.spare_parts_service import find_spare_part
from app.formatters.spare_parts_formatter import format_spare_part
from app.interfaces.max_bot.screen import Screen
from app.interfaces.max_bot.button import Button

class Handler:
    def __init__(self, navigator, start_screen, user_state, faults, parameters,spare_parts):
        self.navigator = navigator
        self.start_screen = start_screen
        self.user_state = user_state
        self.faults = faults
        self.parameters = parameters
        self.spare_parts = spare_parts

    def handle_update(self, update):
        update_type = update.get("update_type")

        if update_type == "bot_started":
            return self.start_screen

        if update_type == "message_callback":
            payload = update["callback"]["payload"]
            user_id = update["callback"]["user"]["user_id"]

            if payload == "pf_525_fault_search":
                self.user_state.set(
                    user_id,
                    {
                        "action": "fault_search",
                        "manufacturer": "allen_bradley",
                        "model": "pf_525",
                    },
                )

                return self.navigator.get_screen("pf_525_fault_input")

            if payload == "pf_525_parameters":
                message = format_parameters(self.parameters)

                return Screen(
                    title="pf_525_parameters",
                    text=message,
                    buttons=[
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

            if payload == "bodymaker":
                self.user_state.set(
                    user_id,
                    {
                        "action": "spare_part_search",
                        "equipment": "bodymaker",
                    },
                )

                return self.navigator.get_screen(
                    "bodymaker_spare_part_input"
    )

            self.user_state.clear(user_id)

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

            if state["action"] == "spare_part_search":
                spare_parts = find_spare_part(self.spare_parts, text)
                message = format_spare_part(text, spare_parts)

                self.user_state.clear(user_id)

                return Screen(
                    title="spare_part_result",
                    text=message,
                    buttons=[
                        Button(
                            text="🔍 Искать другую запчасть",
                            payload="bodymaker",
                        ),
                        Button(
                            text="⬅ Назад",
                            payload="spare_parts_menu",
                        ),
                        Button(
                            text="🏠 Главное меню",
                            payload="main_menu",
                        ),
                    ],
                )

        return None