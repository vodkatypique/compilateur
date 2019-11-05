import re


class Programme():
    def __init__(self):
        self.pile = list()
        self.pointeur_pile = 0

        self.pcode = list()
        self.pointeur_instruction = 0
        self.INST = None

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

    #def runPcode(self):
    #    while(True):
    #        self.INST = self.pcode[self.pointeur_instruction]
    #        print(self.INST)
    #        eval("self." + self.INST)

    def convert_parenthese_and_run(self):
        while(True):
            self.INST = self.pcode[self.pointeur_instruction]
            self.INST = self.INST.split(" ")
            argument = [int(arg) for arg in self.INST[1:]]
            getattr(self, self.INST[0])(*argument)


class AnalyseurLexical():
    """ brouillon:
        self.CONSTS = "^((const " + "(" + self.ID[1:-1] + " = [0-9]+;)+)|())$"
        self.VARS = "^((var " + self.ID[1:-1] + "(, " + self.ID[1:-1] + ")*;)|())$"
        self.LIRE = "^read (" + self.ID[1:-1] + "(, " + self.ID[1:-1] + ")*\)$"
        self.RELOP = "^(=|<>|<|>|<=|>=)$"
        self.ADDOP = "^(+|-)$"
        self.MULOP = "^(*|/)$"
        
        self.EXPR = "^" + self.TERM[1:-1] + "( " + self.ADDOP[1:-1] + " " + self.TERM[1:-1] + ")*$"

        self.FACT = "^(" + self.ID[1:-1] + "|[0-9]+|" + "\(" + self.EXPR + "\))$"

        self.TERM = "^" + self.FACT[1:-1] + "( " + self.MULOP[1:-1] + self.FACT[1:-1] + ")*$"

        self.COND = "^" + self.EXPR[1:-1] + " " + self.RELOP[1:-1] + " " + self.EXPR[1:-1] + "$"
        self.ECRIRE = "^write \(" + self.EXPR[1:-1] + "(, " + self.EXPR[1:-1] + ")*\)$"
        self.SI = "^if " + self.COND[1:-1] + " then " + self.INST[1:-1] + "$"
        self.TANTQUE = "^while " + self.COND[1:-1] + " do " + self.INST[1:-1] + "$"    
        self.AFFEC = "^" + self.ID[1:-1] + " := " + self.EXPR[1:-1] + "$"
        
        self.INST = "^(" + self.INSTS[1:-1] + "|" + self.AFFEC[1:-1] + "|" + self.SI[1:-1] + "|" + self.TANTQUE[1:-1] + "|" + self.ECRIRE[1:-1] + "|" + self.LIRE[1:-1] + "|())$"
        self.INSTS = "^begin " + self.INST[1:-1] + "(;" + self.INST[1:-1]+")* end$"
        
        self.BLOCK = "^" + self.CONSTS[1:-1] + " " + self.VARS[1:-1] + self.INSTS[1:-1] + "$"
        self.PROGRAM = "^program " + self.ID[1:-1] + ";" + self.BLOCK[1:-1] + "."
    """
    def __init__(self):
        self.tokens = {
            'id_token': "^(?!^program$|^const$|^var$|^begin$|^end$|^if$|^then$|^while$|^do$|^write$|^read$)[a-zA-Z]+[0-9]*$",
            'num_token': "^[1-9]+[0-9]*$",
            'plus_token': "^\+$",
            'moins_token': "^-$",
            'mul_token': "^\*$",
            'div_token': "^/$",
            'egal_token': "^=$",
            'diff_token': "^!=$",
            'inf_token': "^<$",
            'sup_token': "^>$",
            'inf_egal_token': "^<=$",
            'sup_egal_token': "^>=$",
            'par_ouv_token': "^\($",
            'par_fer_token': "^\)$",
            'virg_token': "^,$",
            'pt_virg_token': "^;$",
            'pt_token': "^.$",
            'affec_token': "^:=$",
            'begin_token': "^begin$",
            'end_token': "^end$",
            'if_token': "^if$",
            'while_token': "^while$",
            'then_token': "^then$",
            'do_token': "^do$",
            'write_token': "^write$",
            'read_token': "^read$",
            'const_token': "^const$",
            'var_token': "^var$",
            'program_token': "^program$",
            # token inconnu ?
        }
        self.index_token = 0
        self.sym = None
        self.val = None
        self.tokens_code = None

    def tokenizeCode(self, code):
        self.tokens_code = code.split()

    def test(self, t):
        print(t)
        print(self.index_token)
        print(self.tokens_code)
        print("\n")

        if not re.match(t, self.tokens_code[self.index_token]):
            print('Erreur : analyseurLexical')
        else:
            self.index_token += 1

    def program(self):
        self.test(self.tokens['program_token'])
        self.test(self.tokens['id_token'])
        self.test(self.tokens['pt_virg_token'])
        self.block()
        if not re.match(self.tokens['pt_virg_token'], self.tokens_code[self.index_token]): #erreur sujet
            print(self.tokens_code[self.index_token])
            print(self.tokens['pt_virg_token'])
            print('Erreur : program')

    def block(self):
        if re.match(self.tokens['const_token'], self.tokens_code[self.index_token]):
            self.consts()
        if re.match(self.tokens['var_token'], self.tokens_code[self.index_token]):
            self.vars()
        self.insts()

    def consts(self):
        self.test(self.tokens['id_token'])
        while not re.match(self.tokens['id_token'], self.tokens_code[self.index_token]):
            self.test(self.tokens['id_token'])  # repetition du test du while, inutile je pense
            self.test(self.tokens['egal_token'])
            self.test(self.tokens['num_token'])
            self.test(self.tokens['pt_virg_token'])

    def vars(self):
        self.test(self.tokens['var_token'])
        self.test(self.tokens['id_token'])
        while re.match(self.tokens['virg_token'], self.tokens_code[self.index_token]):
            self.index_token += 1
            self.test(self.tokens['id_token'])
        self.test(self.tokens['pt_virg_token'])

    def insts(self):
        self.test(self.tokens['begin_token'])
        self.inst()
        while re.match(self.tokens['pt_virg_token'], self.tokens_code[self.index_token]):
            self.index_token += 1
            self.inst()
        self.test(self.tokens['end_token'])

    def inst(self):
        if re.match(self.tokens['id_token'], self.tokens_code[self.index_token]):
            self.affec()
        elif re.match(self.tokens['if_token'], self.tokens_code[self.index_token]):
            self.si()
        elif re.match(self.tokens['while_token'], self.tokens_code[self.index_token]):
            self.tantque()
        elif re.match(self.tokens['begin_token'], self.tokens_code[self.index_token]):
            self.insts()
        elif re.match(self.tokens['write_token'], self.tokens_code[self.index_token]):
            self.ecrire()
        elif re.match(self.tokens['read_token'], self.tokens_code[self.index_token]):
            self.read()

    def affec(self):
        self.test(self.tokens['id_token'])
        self.test(self.tokens['affec_token'])
        self.expr()
    
    def si(self):
        self.test(self.tokens['if_token'])
        self.cond()
        self.test(self.tokens['then_token'])
        self.inst()
    
    def tantque(self):
        self.test(self.tokens['while_token'])
        self.cond()
        self.test(self.tokens['do_token'])
        self.inst()
    
    def ecrire(self):
        self.test(self.tokens['write_token'])
        self.test(self.tokens['par_ouv_token'])
        self.expr()
        while re.match(self.tokens['virg_token'], self.tokens_code[self.index_token]):
            self.index_token += 1
            self.expr()
        self.test(self.tokens['par_fer_token'])

    def lire(self):
        self.test(self.tokens['read_token'])
        self.test(self.tokens['par_ouv_token'])
        self.test(self.tokens['id_token'])
        while re.match(self.tokens['virg_token'], self.tokens_code[self.index_token]):
            self.index_token += 1
            self.test(self.tokens['id_token'])
        self.test(self.tokens['par_fer_token'])

    def expr(self):
        self.term()
        while re.match(self.tokens['plus_token'], self.tokens_code[self.index_token]) or re.match(self.tokens['moins_token'], self.tokens_code[self.index_token]):
            self.index_token += 1
            self.term()

    def cond(self):
        self.expr()
        if re.match(self.tokens['egal_token'], self.tokens_code[self.index_token]) or re.match(self.tokens['diff_token'], self.tokens_code[self.index_token]) or re.match(self.tokens['inf_token'], self.tokens_code[self.index_token]) or re.match(self.tokens['sup_token'], self.tokens_code[self.index_token]) or re.match(self.tokens['inf_egal_token'], self.tokens_code[self.index_token]) or re.match(self.tokens['sup_egal_token'], self.tokens_code[self.index_token]):
            self.index_token += 1
            self.expr()
    
    def term(self):
        self.fact()
        while re.match(self.tokens['mult_token'], self.tokens_code[self.index_token]) or re.match(self.tokens['div_token'], self.tokens_code[self.index_token]):
            self.index_token += 1
            self.fact()
    
    def fact(self):
        if re.match(self.tokens['id_token'], self.tokens_code[self.index_token]) or re.match(self.tokens['num_token'], self.tokens_code[self.index_token]):
            self.index_token += 1
        else:
            self.test(self.tokens['par_ouv_token'])
            self.expr()
            self.test(self.tokens['par_fer'])


"""
#prog = Programme()
#prog.pcode.extend([
    "INT 2",
    "LDA 0",
    "INN",
    "LDA 1",
    "LDA 0",
    "LDV",
    "LDA 1",
    "LDV",
    "ADD",
    "STO",
    "LDA 0",
    "LDV",
    "LDI 0",
    "EQL",
    "BZE 1",
    "LDA 1",
    "LDV",
    "PRN 2",
    "HLT"])

#print(prog.pcode)
#prog.convert_parenthese_and_run()
"""

source = "program P1 ; var VAR1 ; \n begin end ;"
analyseur = AnalyseurLexical()
analyseur.tokenizeCode(source)
analyseur.program()
