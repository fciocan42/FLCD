class GrammarComponent:
    def __init__(self, text: str):
        self._text = text

    @property
    def text(self):
        return self._text

    def __str__(self):
        return self._text

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self._text == other.text

    def __lt__(self, other):
        return self.text < other.text

    def __hash__(self):
        return hash((self._text, ))
