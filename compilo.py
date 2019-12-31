import Programme
import Programme.Analyseur
import parseTxt

"""
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

"""


programme_init = Programme.Programme()
source = parseTxt.parse()
#print(source)
analyseur = Programme.Analyseur.AnalyseurLexical(programme_init)
analyseur.tokenizeCode(source)
analyseur.program()
#print(programme_init.pcode)
programme_init.convert_parenthese_and_run()