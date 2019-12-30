class Programme():
    def __init__(self):
        self.TAILLE_MAX_PC = 20000
        self.pile = list()
        self.pointeur_pile = 0

        self.pcode = list()
        self.pointeur_instruction = 0
        self.INST = None

    from .operationElem import ADD, SUB, MUL, DIV, HLT
    from .comparateur import LEQ, LSS, GEQ, GTR, EQL, NEQ
    from .io import PRN, INN
    from .opePile import LDA, LDI, LDV, STO, INT
    from .branchement import BRN, BZE

    def convert_parenthese_and_run(self):
        self.pointeur_instruction = 0
        while(True):
            print(self.pile, self.pointeur_instruction)
            self.INST = self.pcode[self.pointeur_instruction]
            self.INST = self.INST.split(" ")
            print(self.INST)
            argument = [int(arg) for arg in self.INST[1:]]
            getattr(self, self.INST[0])(*argument)

    def generer1(self, mnemoniques):
        if self.pointeur_instruction == 20000:
            print("erreur taille pc")
        self.pointeur_instruction += 1
        self.pcode.append(mnemoniques)

    def generer2(self, mnemoniques, arg):
        if self.pointeur_instruction == 20000:
            print("erreur taille pc")
        self.pointeur_instruction += 1
        self.pcode.append(mnemoniques + " " + str(arg))