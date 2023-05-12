from Lexer import *
from Parser import *

def main():
    f = open('program.txt')
    string_input = f.read()
    obj = Lexer(string_input)
    tokens = obj.Tokenize()
    print(tokens)
    parser = Parser(tokens)

    program = parser.parse()
    program.execute()

    print(variables)


main()

