from Deliverable.Domain.PIF import PIF
from Deliverable.Domain.SymbolTable import SymbolTable
from Deliverable.Domain.LangSpecs import LangSpecs


class Scanner:
    def __init__(self, input_file, output_file, pif_file, st_file):
        self.language_spec = LangSpecs()
        self.PIF = PIF()
        self.ST = SymbolTable()

        self.input_file = "Source/" + input_file
        self.output_file = output_file
        self.pif_file = pif_file
        self.st_file = st_file

    @staticmethod
    def get_quotes_indexes(line):
        return [index for index, character in enumerate(line) if "\"" in character]

    @staticmethod
    def join_string_constants(quote_indexes, tokens):
        while len(quote_indexes) >= 2:
            first_pos = quote_indexes[0]
            second_pos = quote_indexes[1]

            tokens = tokens[:first_pos] + [''.join(tokens[first_pos: second_pos + 1])] + tokens[second_pos + 1:]

            quote_indexes.pop(0)
            quote_indexes.pop(0)
            for i in range(len(quote_indexes)):
                quote_indexes[i] -= len(tokens[first_pos: second_pos]) - 1

        return tokens

    def split_by_separator(self, line):
        index = 0
        tokens = []
        token = ''

        for char in line:
            if not self.language_spec.isSeparator(char):
                token += line[index]
            else:
                if token:
                    tokens.append(token)
                tokens.append(line[index])
                token = ''

            index += 1

        if token:
            tokens.append(token)

        return self.join_string_constants(self.get_quotes_indexes(tokens), tokens)

    def split_by_operator(self, line):
        index = 0
        tokens = []
        token = ''

        while index in range(len(line)):
            if index == 0 and self.language_spec.isPartOfLogicalOperator(line[index], line):
                return [line]

            if not self.language_spec.isPartOfOperator(line[index]):
                token += line[index]
            else:
                operator = ''

                if index + 1 < len(line):
                    if self.language_spec.isOperator(line[index] + line[index + 1]):
                        operator = line[index: index + 2]
                        index += 1
                    else:
                        operator = line[index]
                else:
                    operator = line[index]

                if token:
                    tokens.append(token)
                tokens.append(operator)
                token = ''

            index += 1

        if token:
            tokens.append(token)

        return tokens

    def split_line(self, line):
        split_line = self.split_by_separator(line)
        line_index = 0
        while line_index < len(split_line):
            result = self.split_by_operator(split_line[line_index])
            split_line = split_line[:line_index] + result + split_line[line_index + 1:]
            line_index += len(result)

        return split_line

    def scan(self):
        with open(self.input_file, 'r') as file:
            line_index = 0
            for line in file:
                line_index += 1
                split_line = self.split_line(line)

                for token in split_line:
                    if self.language_spec.isOperator(token) or self.language_spec.isSeparator(token) \
                            or self.language_spec.isReservedWord(token):
                        if token == ' ':
                            self.PIF.insert("" "", (-1, -1))
                        elif token == '\n':
                            self.PIF.insert("\n", (-1, -1))
                        elif token == '\t':
                            self.PIF.insert("\t", (-1, -1))
                        else:
                            self.PIF.insert(token, (-1, -1))
                    else:
                        if self.language_spec.isConstant(token):
                            if token not in self.ST:
                                self.ST.insert(token)
                            self.PIF.insert("const", self.ST.getPosition(token))
                        elif self.language_spec.isIdentifier(token):
                            if token not in self.ST:
                                self.ST.insert(token)
                            self.PIF.insert("id", self.ST.getPosition(token))
                        else:
                            print(f"Lexical error - line: {line_index} " + token)

                self.print_output()

    def print_output(self):
        with open(self.pif_file, 'w') as file:
            file.write("{:<10} {:<10} \n".format("Code", "Position"))
            for token in self.PIF.content():
                file.write("{:<10} {:<10} \n".format(token[0], str(token[1])))

        with open(self.st_file, 'w') as file:
            file.write("{:<10} {:<10} \n".format("Index", "Values"))

            for index in range(self.ST.capacity):
                values = self.ST[index]
                file.write("{:<10} {:<10} \n".format(index, str(values)))


def tests():
    scanner = Scanner("In.txt", "Out.txt", "ProgramInternalFile.txt", "SymbolTableFile.txt")
    print("Scanner tests passed!")


if __name__ == '__main__':

    scanner = Scanner("p3.txt", "out/Output.txt", "out/PIF.txt", "out/ST.txt")
    scanner.scan()

    tests()
