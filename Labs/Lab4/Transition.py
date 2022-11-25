class Transition:
    def __init__(self, start_state, value, end_state):
        self.startState = start_state
        self.value = value
        self.endState = end_state

    def get_start_state(self):
        return self.startState

    def set_start_state(self, start_state):
        self.startState = start_state

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_end_state(self):
        return self.endState

    def set_end_state(self, end_state):
        self.endState = end_state

    def __str__(self) -> str:
        return str(self.startState) + ' -> ' + str(self.value) + ' -> ' + str(self.endState)
