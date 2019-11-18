import Programme
import Programme.Analyseur


"""
prog = Programme()
prog.pcode.extend([
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
    "PRN",
    "HLT"])

print(prog.pcode)
prog.convert_parenthese_and_run()

"""

programme_init = Programme.Programme()
source = "program P1; const C1 = 2; C2 = 4; var VAR1, VAR2; \n begin write ( C1 * C2 ) end."
analyseur = Programme.Analyseur.AnalyseurLexical(programme_init)
analyseur.tokenizeCode(source)
analyseur.program()
print(programme_init.pcode)

