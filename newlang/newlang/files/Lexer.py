operators_char = {
    "-": "MINUS",
    "+": "PLUS",
    "/": "DEL",
    "*": "MULTY",
    "(": "LPAREN",
    ")": "RPAREN",
    "{": "LBRACE",
    "}": "RBRACE",
    "&": "AND",
    "|": "OR",
    "!": "NOT",
    "=": "EQ",
    ",": "COMMA",
    "^": "POW",
    "==": "EQUALITY",
    ">": "BIG",
    "<": "SMALL",
    "<=": "SMALLEQ",
    ">=": "BIGEQ",
    "print": "PRINT",
    "~": "SQRT"
}

class Lexer:
    def __init__(self, sours):
        self.position = 0
        self.sours = sours
        self.len_sours = len(sours)
        self.tokens = []

    def Tokenize(self):
        while(self.position < self.len_sours):
            current = self.peek(0)
            if (current.isdigit()):
                self.tokenize_number()
            if (current.isalpha()):
                self.tokenize_word()
            elif(current in operators_char.keys()):
                self.tokenize_operator()
            elif(current == '#'):
                self.next()
                self.tokenize_bit_number()
            else:
                self.next()
        return self.tokens


    def tokenize_word(self):
        line_num = ''
        current = self.peek(0)
        while (current.isalpha() or current == '_' or current == '$'):
            line_num += current
            self.next()
            current = self.peek(0)
        if line_num == 'print':
            self.add_Token("PRINT", line_num)
        elif line_num == 'if':
            self.add_Token("IF", line_num)
        elif line_num == 'while':
            self.add_Token("WHILE", line_num)
        elif  line_num == 'for':
            self.add_Token("FOR", line_num)
        else:
            self.add_Token("WORD", line_num)
        return

    def tokenize_bit_number(self):
        line_num = ''
        current = self.peek(0)
        while (current.isdigit() and (int(current) == 0 or int(current) == 1)):
            line_num += current
            self.next()
            current = self.peek(0)
        self.add_Token("BIT", line_num)
        return

    def tokenize_number(self):
        line_num = ''
        current = self.peek(0)
        while(True):
            if(current == '.'):
                if('.' in line_num):
                    raise Exception('invalid symvol \'.\' ')
            elif(not current.isdigit()):
                break
            line_num += current
            self.next()
            current = self.peek(0)
        self.add_Token("NUMBER", line_num)
        return

    def tokenize_operator(self):
        # self.add_Token(operators_char[self.peek(0)], self.peek(0))
        # self.next()
        # return
        if self.peek(1) == '=':
            self.next()
            self.add_Token(operators_char[self.peek(-1) + self.peek(0)], self.peek(-1) + self.peek(0))
        else:
            self.add_Token(operators_char[self.peek(0)], self.peek(0))
        self.next()
        return

    def add_Token(self, Type):
        self.tokens.append({type: ""})
        return

    def add_Token(self, Type, Token):
        self.tokens.append({Type: Token})
        return

    def next(self):
        self.position += 1
        return self.peek(0)

    def peek(self, relativ_position):
        pos = self.position + relativ_position
        if(pos >= self.len_sours):
            return "\0"
        return self.sours[pos]