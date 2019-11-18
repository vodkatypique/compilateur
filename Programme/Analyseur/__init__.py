import re


class AnalyseurLexical():
    def __init__(self, programme):
        self._program = programme
        self.tokens = {
            'id_token': "^(?!^program$|^const$|^var$|^begin$|^end$|^if$|^then$|^while$|^do$|^write$|^read$)[a-zA-Z]+[0-9]*$",
            'keyword': ("^program$|^const$|^var$|^begin$|^end$|^if$|^then$|^while$|^do$|^write$|^read$"),
            'num_token': "^[1-9]+[0-9]*$",
            'plus_token': "^\+$",
            'moins_token': "^-$",
            'mult_token': "^\*$",
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
        self.tableDesSymboles = []
        self.ensembleNom = set()
    
    def tokenizeCode(self, code):
        self.tokens_code = code.replace(";", " ;").replace(",", " ,").replace(".", " .").split()

    def test(self, t):
        if not re.match(t, self.tokens_code[self.index_token]):
            print('Erreur : analyseurLexical, attendu : ' + self.tokens_code[self.index_token])
        else:
            self.index_token += 1
    
    from .tableSymbole import chercherSym, entrerSym
    from .structures import program, affec, block, cond, consts, ecrire, expr, fact, inst, insts, lire, si, tantque, term, vars
    