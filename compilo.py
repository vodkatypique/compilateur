class Memoire():
    def __init__(self):
        self.pile = list()
        self.pointeur_pile = 0

        self.pcode = list()
        self.pointeur_instruction = 0

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

    def PRN(self):
        print(self.pile.pop())
        self.pointeur_instruction += 1

    def INN(self):
        self.pile[self.pile.pop()] = int(input())
        self.pointeur_instruction += 1

    def INT(self, c):
        self.pointeur_pile += c
        if c > 0:
            self.pile.extend([0 for _ in range(c)])
        self.pointeur_instruction += 1

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

    def BRN(self, i):
        self.pointeur_instruction = i

    def BZE(self, i):
        if self.pile.pop() == 0:
            self.pointeur_instruction = i-1
        self.pointeur_instruction += 1

    def HLT(self):
        quit()

    def runPcode(self):
        while(True):
            eval("self." + self.pcode[self.pointeur_instruction])


prog = Memoire()
prog.pcode.extend([
    "INT(2)",
    "LDA(0)",
    "INN()",
    "LDA(1)",
    "LDA(0)",
    "LDV()",
    "LDA(1)",
    "LDV()",
    "ADD()",
    "STO()",
    "LDA(0)",
    "LDV()",
    "LDI(0)",
    "EQL()",
    "BZE(1)",
    "LDA(1)",
    "LDV()",
    "PRN()",
    "HLT()"])

print(prog.pcode)
prog.runPcode()
