from app.formatters.fault_formatter import format_fault
from app.formatters.parameters_formatter import format_parameters
from app.formatters.spare_parts_formatter import (
    format_spare_part,
)
from app.interfaces.max_bot.button import Button
from app.interfaces.max_bot.screen import Screen
from app.interfaces.max_bot.vfd_catalog import VFD_CATALOG
from app.interfaces.max_bot.vfd_screens import (
    make_model_menu_screen,
    make_fault_input_screen,
    make_vfd_actions_screen,
)
from app.services.faults_service import find_fault
from app.services.spare_parts_service import find_spare_part


class Handler:
    def __init__(
        self,
        navigator,
        start_screen,
        user_state,
        vfd_data_loader,
        spare_parts_data_loader,
    ):
        self.navigator = navigator
        self.start_screen = start_screen
        self.user_state = user_state
        self.vfd_data_loader = vfd_data_loader
        self.spare_parts_data_loader = (
            spare_parts_data_loader
        )

    def _get_vfd_context(self, user_id):
        state = self.user_state.get(user_id)

        if state is None:
            return None

        manufacturer_id = state.get("manufacturer")
        model_id = state.get("model")

        manufacturer_data = VFD_CATALOG.get(
            manufacturer_id
        )

        if manufacturer_data is None:
            return None

        model_data = manufacturer_data["models"].get(
            model_id
        )

        if model_data is None:
            return None

        return (
            state,
            manufacturer_data,
            model_data,
        )

    def _handle_manufacturer_selection(
        self,
        payload,
    ):
        payload_parts = payload.split(":")

        if len(payload_parts) != 2:
            return self.navigator.fallback_screen

        action, manufacturer_id = payload_parts

        if action != "vfd_manufacturer":
            return self.navigator.fallback_screen

        manufacturer_data = VFD_CATALOG.get(
            manufacturer_id
        )

        if manufacturer_data is None:
            return self.navigator.fallback_screen

        return make_model_menu_screen(
            manufacturer_id=manufacturer_id,
            manufacturer_data=manufacturer_data,
        )

    def _handle_vfd_selection(self, user_id, payload):
        payload_parts = payload.split(":")

        if len(payload_parts) != 3:
            return self.navigator.fallback_screen

        action, manufacturer_id, model_id = payload_parts

        if action != "vfd_select":
            return self.navigator.fallback_screen

        manufacturer_data = VFD_CATALOG.get(
            manufacturer_id
        )

        if manufacturer_data is None:
            return self.navigator.fallback_screen

        model_data = manufacturer_data["models"].get(
            model_id
        )

        if model_data is None:
            return self.navigator.fallback_screen

        self.user_state.set(
            user_id,
            {
                "manufacturer": manufacturer_id,
                "model": model_id,
                "action": None,
            },
        )

        return make_vfd_actions_screen(
            manufacturer_id=manufacturer_id,
            manufacturer_data=manufacturer_data,
            model_data=model_data,
        )

    def _handle_fault_search(self, user_id):
        context = self._get_vfd_context(user_id)

        if context is None:
            return self.navigator.fallback_screen

        state, manufacturer_data, model_data = context

        self.user_state.set(
            user_id,
            {
                "manufacturer": state["manufacturer"],
                "model": state["model"],
                "action": "fault_search",
            },
        )

        return make_fault_input_screen(
            model_data=model_data,
        )

    def _handle_parameters(self, user_id):
        context = self._get_vfd_context(user_id)

        if context is None:
            return self.navigator.fallback_screen

        state, manufacturer_data, model_data = context

        parameters = self.vfd_data_loader(
            manufacturer=state["manufacturer"],
            model=state["model"],
            data_type="parameters",
        )

        message = format_parameters(parameters)

        return Screen(
            title="vfd_parameters",
            text=message,
            buttons=[
                Button(
                    text="⬅ Назад",
                    payload="vfd_current",
                ),
                Button(
                    text="🏠 Главное меню",
                    payload="main_menu",
                ),
            ],
        )

    def _handle_current_vfd(self, user_id):
        context = self._get_vfd_context(user_id)

        if context is None:
            return self.navigator.fallback_screen

        state, manufacturer_data, model_data = context

        return make_vfd_actions_screen(
            manufacturer_id=state["manufacturer"],
            manufacturer_data=manufacturer_data,
            model_data=model_data,
        )

    def _handle_fault_message(
        self,
        user_id,
        text,
        state,
    ):
        faults = self.vfd_data_loader(
            manufacturer=state["manufacturer"],
            model=state["model"],
            data_type="faults",
        )

        fault = find_fault(faults, text)
        message = format_fault(text, fault)

        self.user_state.set(
            user_id,
            {
                "manufacturer": state["manufacturer"],
                "model": state["model"],
                "action": None,
            },
        )

        return Screen(
            title="fault_result",
            text=message,
            buttons=[
                Button(
                    text="🔍 Искать другую ошибку",
                    payload="vfd_fault_search",
                ),
                Button(
                    text="⬅ Назад",
                    payload="vfd_current",
                ),
                Button(
                    text="🏠 Главное меню",
                    payload="main_menu",
                ),
            ],
        )

    def _handle_spare_part_message(
        self,
        user_id,
        text,
        state,
    ):
        spare_parts_data = (
            self.spare_parts_data_loader(
                data_type=state["data_type"],
            )
        )

        spare_parts = find_spare_part(
            spare_parts_data,
            text,
        )

        message = format_spare_part(
            text,
            spare_parts,
        )

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

    def handle_update(self, update):
        update_type = update.get("update_type")

        if update_type == "bot_started":
            return self.start_screen

        if update_type == "message_callback":
            payload = update["callback"]["payload"]
            user_id = update["callback"]["user"]["user_id"]

            if payload.startswith(
                "vfd_manufacturer:"
            ):
                return (
                    self._handle_manufacturer_selection(
                        payload=payload,
                    )
                )

            if payload.startswith("vfd_select:"):
                return self._handle_vfd_selection(
                    user_id=user_id,
                    payload=payload,
                )

            if payload == "vfd_fault_search":
                return self._handle_fault_search(user_id)

            if payload == "vfd_parameters":
                return self._handle_parameters(user_id)

            if payload == "vfd_current":
                return self._handle_current_vfd(user_id)

            if payload == "bodymaker":
                self.user_state.set(
                    user_id,
                    {
                        "action": "spare_part_search",
                        "data_type": "bm",
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
                return self._handle_fault_message(
                    user_id=user_id,
                    text=text,
                    state=state,
                )

            if state["action"] == "spare_part_search":
                return self._handle_spare_part_message(
                    user_id=user_id,
                    text=text,
                    state=state,
                )

        return None