def ADD(self):
    ajout = self.pile.pop()+self.pile.pop()
    self.pile.append(ajout)
    self.pointeur_instruction += 1


def SUB(self):
    soustraction = self.pile.pop()-self.pile.pop()
    self.pile.append(soustraction)
    self.pointeur_instruction += 1


def MUL(self):
    multi = self.pile.pop()*self.pile.pop()
    self.pile.append(multi)
    self.pointeur_instruction += 1


def DIV(self):
    divi = self.pile.pop()/self.pile.pop()
    self.pile.append(divi)
    self.pointeur_instruction += 1


def HLT(self):
    quit()