from Transition import Transition


class FiniteAutomata:
    def __init__(self):
        self.states = []
        self.initial_state = ''
        self.end_states = []
        self.transitions = []
        self.alphabet = []

    def read_from_file(self, file='fa.in'):
        with open(file, 'r') as file:
            line_index = -1
            for line in file:
                line_index += 1
                match line_index:
                    case 0:
                        self.states = line.split('\n')[0].split(',')
                    case 1:
                        self.alphabet = line.split('\n')[0].split(',')
                    case 2:
                        self.initial_state = line.split('\n')[0]
                    case 3:
                        self.end_states = line.split('\n')[0]
                    case _:
                        transition = line.split('\n')[0].split(',')
                        self.transitions.append(Transition(transition[0], transition[1], transition[2]))

    def get_next_state(self, current_state, value):
        for transition in self.transitions:
            if (current_state == transition.get_start_state()) & (transition.get_value() == value):
                return transition.endState
        return None

    def is_accepted(self, variable):
        current_state = self.initial_state
        for character in variable:
            current_state = self.get_next_state(current_state, character)
        return current_state in self.end_states

    def states_str(self):
        result_str = '\nStates | '
        for elem in self.states:
            result_str += str(elem) + ' '
        return result_str + '\n'

    def alphabet_str(self):
        result_str = '\nAlphabet | '
        for elem in self.alphabet:
            result_str += str(elem) + ' '
        return result_str + '\n'

    def transition_str(self):
        result_str = '\nTransitions\n'
        for elem in self.transitions:
            result_str += str(elem) + ' \n'
        return result_str

    def initial_state_str(self):
        return '\nInitial state | ' + str(self.initial_state) + '\n'

    def final_states_str(self):
        result_str = '\nFinal states | '
        for elem in self.end_states:
            result_str += str(elem) + ' '
        return result_str + '\n'
