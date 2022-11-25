import re


class LangSpecs:
    def __init__(self):
        self.__operators = ["!=", "+", "-", "*", "/", "%", "<", "<=", "==", ">=", ">", "=", "|", "->"]
        self.__logical_operators = ["and", "or", "not"]
        self.__separators = ["{", "}", "(", ")", "[", "]", ";", ",", ".", "#", " ", "\n"]
        self.__reserved_words = ["fun", "define", "case", "of", "end", "when", "read", "write"]

    def isOperator(self, token):
        return token in self.__operators

    def isPartOfOperator(self, chars):
        for operator in self.__operators:
            if chars in operator:
                return True
        return False

    def isPartOfLogicalOperator(self, char, token):
        if char == "a" and token == "and":
            return True
        elif char == "o" and token == "or":
            return True
        elif char == "n" and token == "not":
            return True
        else:
            return False

    def isSeparator(self, token):
        return token in self.__separators

    def isReservedWord(self, token):
        return token in self.__reserved_words

    def isIdentifier(self, token):
        return re.match(r'^[_a-zA-Z]([_a-zA-Z]|[0-9]|_){,30}$', token) is not None

    def isConstant(self, token):
        return re.match('(^(0|[\+\-]?[1-9][0-9]*))$|(^"[a-z|A-Z| |!|?|.|\']"*)$|^\'.\'$|^\".*\"$', token) is not None
