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
#source = "program P1; var A, B; \n begin read ( A ); read ( B ); write ( A ); write ( B ) end."
source = "program P1; var A, B; begin read ( A ); while A != 0 do begin read ( A ); B := A + B; end; write ( B ) end."
analyseur = Programme.Analyseur.AnalyseurLexical(programme_init)
analyseur.tokenizeCode(source)
analyseur.program()
print(programme_init.pcode)
programme_init.convert_parenthese_and_run()