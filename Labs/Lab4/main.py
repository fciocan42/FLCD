from FiniteAutomata import FiniteAutomata


def print_menu():
    print('1 | Print set of states')
    print('2 | Print alphabet')
    print('3 | Print transitions')
    print('4 | Print initial state')
    print('5 | Print final states')
    print('6 | Check if string is accepted ')


def check():
    given_string = input('Give a string: ')
    if fa.is_accepted(given_string):
        return '\nAccepted\n'
    else:
        return '\nNot accepted\n'


if __name__ == '__main__':
    fa = FiniteAutomata()
    fa.read_from_file()
    cmd_dict = {
        '1': fa.states_str,
        '2': fa.alphabet_str,
        '3': fa.transition_str,
        '4': fa.initial_state_str,
        '5': fa.final_states_str,
        '6': check
    }
    while True:
        print_menu()
        option = input('Enter command number: ').strip()
        if option in cmd_dict.keys():
            print(cmd_dict[option]())
        else:
            print('Bye')
            break
