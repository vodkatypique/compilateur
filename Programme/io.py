def PRN(self):
    print(self.pile.pop())
    self.pointeur_instruction += 1


def INN(self):
    self.pile[self.pile[-1]] = int(input())
    self.pointeur_instruction += 1
