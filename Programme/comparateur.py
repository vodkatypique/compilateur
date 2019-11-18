def EQL(self):
    sommet = self.pile.pop()
    sous_sommet = self.pile.pop()
    self.pile.append(int(sommet == sous_sommet))
    self.pointeur_instruction += 1


def NEQ(self):
    sommet = self.pile.pop()
    sous_sommet = self.pile.pop()
    self.pile.append(int(sommet != sous_sommet))
    self.pointeur_instruction += 1


def GTR(self):
    sommet = self.pile.pop()
    sous_sommet = self.pile.pop()
    self.pile.append(int(sommet > sous_sommet))
    self.pointeur_instruction += 1


def LSS(self):
    sommet = self.pile.pop()
    sous_sommet = self.pile.pop()
    self.pile.append(int(sommet < sous_sommet))
    self.pointeur_instruction += 1


def GEQ(self):
    sommet = self.pile.pop()
    sous_sommet = self.pile.pop()
    self.pile.append(int(sommet >= sous_sommet))
    self.pointeur_instruction += 1


def LEQ(self):
    sommet = self.pile.pop()
    sous_sommet = self.pile.pop()
    self.pile.append(int(sommet <= sous_sommet))
    self.pointeur_instruction += 1