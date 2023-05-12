from Variables import *
from Statement import *
class AssigmentStatement(Statement):
    def __init__ (self, variable, result):
        self.variable = variable
        self.result = result

    def execute(self):
        super().execute()
        setVariables(self.variable, self.result.eval())


