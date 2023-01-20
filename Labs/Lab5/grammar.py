import re

from typing import List, Set, Type

from grammar_components.grammar_component import GrammarComponent
from grammar_components.terminal import Terminal
from grammar_components.non_terminal import NonTerminal
from production import Production


class Grammar:
    def __init__(
        self,
        statements: List[str],
        equal_symbol: str = '=',
        or_operator: str = '|',
    ):
        self._statements: List[str] = statements
        self._equal_symbol: str = equal_symbol
        self._or_operator: str = or_operator
        self.productions: List[Production] = self.process()

    @property
    def equal_symbol(self):
        return self._equal_symbol

    @property
    def or_operator(self):
        return self._or_operator

    def process(self) -> List[Production]:
        productions: List[Production] = []
        for statement in self._statements:
            lhs, rhs = re.split(rf" {re.escape(self._equal_symbol)} ", statement)
            lhs_options, rhs_options = [
                re.split(rf' {re.escape(self._or_operator)} ', side)
                for side
                in [lhs, rhs]
            ]

            for lhs_option in lhs_options:
                lhs_components: List[GrammarComponent] = self._string_to_components(lhs_option)
                for rhs_options in rhs_options:
                    rhs_components: List[GrammarComponent] = self._string_to_components(rhs_options)
                    productions.append(Production(lhs_components, rhs_components))

        return sorted(productions)

    @staticmethod
    def _string_to_components(text: str):
        components: List[GrammarComponent] = []
        tokens: List[str] = text.split(' ')

        for token in (t for t in tokens if t):
            token_class: Type[GrammarComponent] = Terminal if token.startswith('"') else NonTerminal
            components.append(token_class(token))

        return components

    def get_non_terminals(self) -> Set[NonTerminal]:
        non_terminals_set: Set[NonTerminal] = set()
        for production in self.productions:
            non_terminals_set.update(production.get_non_terminals())
        return non_terminals_set

    def get_terminals(self) -> Set[Terminal]:
        terminals_set: Set[Terminal] = set()
        for production in self.productions:
            terminals_set.update(production.get_terminals())
        return terminals_set

    def get_productions(self) -> Set[Production]:
        return set(self.productions)

    def get_productions_for_non_terminal(self, non_terminal: NonTerminal) -> Set[Production]:
        return set(filter(lambda p: p.does_contain_non_terminal(non_terminal), self.productions))

    def get_productions_with_non_terminal_lhs(self, non_terminal: NonTerminal) -> Set[Production]:
        return set(filter(lambda p: p.starts_with_non_terminal(non_terminal), self.productions))

    def is_context_free(self) -> bool:
        for production in self.productions:
            if len((lhs := production.lhs)) != 1 and not isinstance(lhs[0], NonTerminal):
                return False
        return True
