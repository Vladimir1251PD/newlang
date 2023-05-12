from Statement import *
class ForStatement(Statement):
    def __init__(self, start, finish, block):
        self.start = start
        self.finish = finish
        self.block = block
    def execute(self):
        super().execute()
        for i in range(self.start, self.finish, 1):
            self.block.execute()
