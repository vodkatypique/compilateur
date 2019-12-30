import re
from .. import *

def program(self):
    self.classeDuToken = "programme"
    self.test(self.tokens['program_token'])
    self.test(self.tokens['id_token'])

    self.entrerSym("programm")

    self.test(self.tokens['pt_virg_token'])
    self.block()
    self._program.generer1("HLT")
    
    if not re.match(self.tokens['pt_token'], self.tokens_code[self.index_token]): # erreur sujet
        print(self.tokens_code[self.index_token])
        print(self.tokens['pt_token'])
        print('Erreur : program')


def block(self):
    if re.match(self.tokens['const_token'], self.tokens_code[self.index_token]):
        self.consts()
    if re.match(self.tokens['var_token'], self.tokens_code[self.index_token]):
        self.vars()
    
    offset = len(self.tableDesSymboles)-1
    # print(self._program.generer2)
    self._program.generer2("INT", offset)
    
    self.insts()


def consts(self):
    self.test(self.tokens['const_token'])
    self.test(self.tokens['id_token'])
    self.entrerSym("const")

    self.test("=")

    self.test(self.tokens['num_token'])
    self.test(self.tokens['pt_virg_token'])

    while not re.match(self.tokens['keyword'], self.tokens_code[self.index_token]):
        self.test(self.tokens['id_token'])
            
        self.entrerSym("const")

        self.test("=")
        
        self.test(self.tokens['num_token'])
        self.test(self.tokens['pt_virg_token'])


def vars(self):
    self.test(self.tokens['var_token'])
    self.test(self.tokens['id_token'])

    self.entrerSym("var")

    while re.match(self.tokens['virg_token'], self.tokens_code[self.index_token]):
        self.index_token += 1
        self.test(self.tokens['id_token'])
            
        self.entrerSym("var")

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
        self.lire()


def affec(self):
    self.compareSym(self.tokens_code[self.index_token], "var")
    self.test(self.tokens['id_token'])
    self._program.generer2("LDA", self.chercherSym(self.tokens_code[self.index_token-1]))
    self.test(self.tokens['affec_token'])
    self.expr()
    self._program.generer1("STO")


def si(self):
    self.test(self.tokens['if_token'])
    self.cond()
    self.test(self.tokens['then_token'])
    self.next_inst()
    self._program.generer2("BZE", 0)
    self.inst()
    self.next_inst()
    self.remplir_inst()
    

def tantque(self):
    self.test(self.tokens['while_token'])
    debut = len(self._program.pcode)
    self.cond()
    self.test(self.tokens['do_token'])
    self.next_inst()
    self._program.generer2("BZE", 0)
    self.inst()
    self._program.generer2("BRN", debut)
    self.next_inst()
    self.remplir_inst()
    

def ecrire(self):
    self.test(self.tokens['write_token'])
    self.test(self.tokens['par_ouv_token'])
    self.expr()
    self._program.generer1("PRN")
    while re.match(self.tokens['virg_token'], self.tokens_code[self.index_token]):
        self.index_token += 1
        self.expr()
        self._program.generer1("PRN")
    self.test(self.tokens['par_fer_token'])


def lire(self):
    self.test(self.tokens['read_token'])
    self.test(self.tokens['par_ouv_token'])
    self.test(self.tokens['id_token'])
    self._program.generer2("LDA", self.chercherSym(self.tokens_code[self.index_token-1]))
    self._program.generer1("INN")
    while re.match(self.tokens['virg_token'], self.tokens_code[self.index_token]):
        self.index_token += 1
        self.test(self.tokens['id_token'])
        self._program.generer2("LDA", self.chercherSym(self.tokens_code[self.index_token-1]))
        self._program.generer1("INN")
    self.test(self.tokens['par_fer_token'])


def expr(self):
    op = None
    self.term()
    while re.match(self.tokens['plus_token'], self.tokens_code[self.index_token]) or re.match(self.tokens['moins_token'], self.tokens_code[self.index_token]):
        op = self.tokens_code[self.index_token]
        self.index_token += 1
        self.term()
        if re.match(self.tokens['plus_token'], op):
            self._program.generer1("ADD")
        else:
            self._program.generer1("SUB")


def cond(self):
    self.expr()
    if re.match(self.tokens['egal_token'], self.tokens_code[self.index_token]) or re.match(self.tokens['diff_token'], self.tokens_code[self.index_token]) or re.match(self.tokens['inf_token'], self.tokens_code[self.index_token]) or re.match(self.tokens['sup_token'], self.tokens_code[self.index_token]) or re.match(self.tokens['inf_egal_token'], self.tokens_code[self.index_token]) or re.match(self.tokens['sup_egal_token'], self.tokens_code[self.index_token]):
        op = self.tokens_code[self.index_token]
        self.index_token += 1
        self.expr()
        if re.match(self.tokens['egal_token'], op):
            self._program.generer1("EQL")
        elif re.match(self.tokens['diff_token'], op):
            self._program.generer1("NEQ")
        elif re.match(self.tokens['inf_token'], op):
            self._program.generer1("LSS")
        elif re.match(self.tokens['sup_token'], op):
            self._program.generer1("GTR")
        elif re.match(self.tokens['inf_egal_token'], op):
            self._program.generer1("LEQ")
        elif re.match(self.tokens['sup_egal_token'], op):
            self._program.generer1("GEQ")


def term(self):
    op = None
    self.fact()
    while re.match(self.tokens['mult_token'], self.tokens_code[self.index_token]) or re.match(self.tokens['div_token'], self.tokens_code[self.index_token]):
        op = self.tokens_code[self.index_token]
        self.index_token += 1
        self.fact()
        if re.match(self.tokens['mult_token'], op):
            self._program.generer1("MUL")
        else:
            self._program.generer1("DIV")


def fact(self):
    if re.match(self.tokens['id_token'], self.tokens_code[self.index_token]) or re.match(self.tokens['num_token'], self.tokens_code[self.index_token]):
        if re.match(self.tokens['id_token'], self.tokens_code[self.index_token]):
            self._program.generer2("LDA", self.chercherSym(self.tokens_code[self.index_token]))
            self._program.generer1("LDV")
        self.index_token += 1
    else:
        print(self.tokens['num_token'], self.tokens_code[self.index_token])
        self.test(self.tokens['par_ouv_token'])
        self.expr()
        self.test(self.tokens['par_fer_token'])