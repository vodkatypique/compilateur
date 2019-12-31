import Programme
import Programme.Analyseur
import parseTxt

if __name__ == "__main__": 
    programme_init = Programme.Programme()
    source = parseTxt.parse()
    #print(source)
    analyseur = Programme.Analyseur.AnalyseurLexical(programme_init)
    analyseur.tokenizeCode(source)
    analyseur.program()
    #print(programme_init.pcode)
    programme_init.convert_parenthese_and_run()