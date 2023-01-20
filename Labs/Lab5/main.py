from typing import Iterable, Optional

from constants import INPUT_FILE
from grammar import Grammar
from file_io import read_lines


def print_iter(iterable: Iterable, elem_prefix: Optional[str] = None):
    if elem_prefix is None:
        elem_prefix = ''

    for elem in iterable:
        print(elem_prefix + str(elem))


def print_grammar_info(grammar):
    section_separator = f"\n{'-' * 100}\n"

    print(section_separator)

    print(f"\nIs grammar context free?: {grammar.is_context_free()}\n")

    print(f"{section_separator}\nTerminals:\n")
    print_iter(grammar.get_terminals())

    non_terminals = grammar.get_non_terminals()
    print(f"{section_separator}\nNon-terminals:\n")
    print_iter(non_terminals)

    productions = grammar.get_productions()
    print(f"{section_separator}\nProductions:\n")
    print_iter(productions)

    print(f"{section_separator}\nProductions for every non-terminal:\n")
    for nt in non_terminals:
        print(f"\n{str(nt)}")
        print_iter(grammar.get_productions_for_non_terminal(nt), elem_prefix="\t")

    print(section_separator)


def read_grammar():
    input_file_contents = read_lines(INPUT_FILE)

    grammar = Grammar(input_file_contents)
    grammar.process()
    return grammar


if __name__ == "__main__":
    print_grammar_info(read_grammar())
