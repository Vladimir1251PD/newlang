class UnaryExpression:
    def __init__(self, operation, expr1):
        self.operation = operation
        self.expr1 = expr1

    def eval(self):
        if (self.operation == "-"):
            return -self.expr1.eval()

