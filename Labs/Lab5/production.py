from typing import List, Set

from grammar_components.grammar_component import GrammarComponent
from grammar_components.terminal import Terminal
from grammar_components.non_terminal import NonTerminal


class Production:
    def __init__(self, lhs: List[GrammarComponent], rhs: List[GrammarComponent]):
        self._lhs: List[GrammarComponent] = lhs
        self._rhs: List[GrammarComponent] = rhs

    @property
    def lhs(self):
        return self._lhs

    @property
    def rhs(self):
        return self._rhs

    def __str__(self):
        string_representation = ""

        for component in self._lhs:
            string_representation += str(component) + ' '

        string_representation += "= "

        for component in self._rhs:
            string_representation += str(component) + ' '

        return string_representation[:-1]

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self._lhs == other.lhs
            and self._rhs == other.rhs
        )

    def __lt__(self, other):
        same_lhs = self._lhs == other.lhs
        return self._rhs < other.rhs if same_lhs else self._lhs < other.lhs

    def __hash__(self):
        return hash(
            (tuple(self._lhs), tuple(self._rhs))
        )

    def get_terminals(self) -> Set[Terminal]:
        terminal_set: Set[Terminal] = set()
        for component in self._lhs + self._rhs:
            if isinstance(component, Terminal):
                terminal_set.add(component)
        return terminal_set

    def get_non_terminals(self) -> Set[NonTerminal]:
        non_terminal_set: Set[NonTerminal] = set()
        for component in self._lhs + self._rhs:
            if isinstance(component, NonTerminal):
                non_terminal_set.add(component)
        return non_terminal_set

    def does_contain_non_terminal(self, non_terminal: NonTerminal):
        return non_terminal in self._lhs + self._rhs

    def starts_with_non_terminal(self, non_terminal: NonTerminal):
        return len(self._lhs) == 1 and self._lhs[0] == non_terminal

