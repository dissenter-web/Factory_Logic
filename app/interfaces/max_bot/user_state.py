class UserState:
    def __init__(self):
        self._states = {}

    def set(self, user_id, state):
        self._states[user_id] = state

    def get(self, user_id):
        return self._states.get(user_id)

    def clear(self, user_id):
        self._states.pop(user_id, None)