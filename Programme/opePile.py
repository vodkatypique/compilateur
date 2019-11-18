def LDI(self, v):
    self.pile.append(int(v))
    self.pointeur_instruction += 1


def LDA(self, a):
    adresse = a
    self.pile.append(adresse)
    self.pointeur_instruction += 1


def LDV(self):
    self.pile[-1] = self.pile[self.pile[-1]]
    self.pointeur_instruction += 1


def STO(self):
    valeur = self.pile.pop()
    adresse = self.pile.pop()
    self.pile[adresse] = valeur
    self.pointeur_instruction += 1

def INT(self, c):
    self.pointeur_pile += c
    if c > 0:
        self.pile.extend([0 for _ in range(c)])
    self.pointeur_instruction += 1
