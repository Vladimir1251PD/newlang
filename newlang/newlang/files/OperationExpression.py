class OperationExpression:
    def __init__(self, operation, expr1, expr2):
        self.operation = operation
        self.expr1 = expr1
        self.expr2 = expr2


    def eval(self):
        if(self.operation == "+"):
            return self.expr1.eval() + self.expr2.eval()
        elif (self.operation == "*"):
            return self.expr1.eval() * self.expr2.eval()
        elif (self.operation == "/"):
            return self.expr1.eval() / self.expr2.eval()
        elif (self.operation == "-"):
            return self.expr1.eval() - self.expr2.eval()
        elif (self.operation == "^"):
            return self.expr1.eval() ** self.expr2.eval()
        elif (self.operation == '<='):
            return self.expr1.eval() <= self.expr2.eval()
        elif (self.operation == '>='):
            return self.expr1.eval() >= self.expr2.eval()
        elif self.operation == '<':
            return self.expr1.eval() < self.expr2.eval()
        elif self.operation == '>':
            return self.expr1.eval() > self.expr2.eval()
        elif self.operation == '==':
            return self.expr1.eval() == self.expr2.eval()

        # binary_operation
        elif (self.operation == "&"):
            newline = ''
            line_expr1 = bin(self.expr1.eval())
            line_expr2 = bin(self.expr2.eval())
            line_expr1 = line_expr1[len(line_expr1) - 1:1:-1]
            line_expr2 = line_expr2[len(line_expr2) - 1:1:-1]
            len_min = min(len(line_expr1), len(line_expr2))
            for i in range(len_min):
                if (line_expr1[i] == '1' and line_expr2[i] == '1'):
                    newline += '1'
                else:
                    newline += '0'
            newline = newline[::-1]
            index = 0
            for i in range(len(newline)):
                if (newline[i] == 1):
                    index = i
                    break
            newline = newline[index::]
            if (len(newline) != 0):
                return int(newline, 2)
            else:
                return 0

        elif (self.operation == "|"):
            newline = ''
            line_expr1 = bin(self.expr1.eval())
            line_expr2 = bin(self.expr2.eval())
            line_expr1 = line_expr1[len(line_expr1) - 1:1:-1]
            line_expr2 = line_expr2[len(line_expr2) - 1:1:-1]
            len_max = max(len(line_expr1), len(line_expr2))
            len_min = min(len(line_expr1), len(line_expr2))
            for i in range(len_max):
                if (i < len_min):
                    if (line_expr1[i] == '0' and line_expr2[i] == '0'):
                        newline += '0'
                    else:
                        newline += '1'
                else:
                    if (len(line_expr1) > len(line_expr2)):
                        if (line_expr1[i] == '1'):
                            newline += '1'
                        else:
                            newline += '0'
                    else:
                        if (line_expr2[i] == '1'):
                            newline += '1'
                        else:
                            newline += '0'
            newline = newline[::-1]
            return int(newline, 2)

