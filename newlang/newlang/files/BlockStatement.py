from Statement import *
class BlockStatement(Statement):
    #statements = []
    def __init__(self):
        self.statements = []

    def add(self, statement):
        self.statements.append(statement)

    def execute(self):
        super().execute()
        for i in range(len(self.statements)):
            self.statements[i].execute()


