def BRN(self, i):
    self.pointeur_instruction = i


def BZE(self, i):
    if self.pile.pop() == 0:
        self.pointeur_instruction = i-1
    self.pointeur_instruction += 1