def entrerSym(self, classe):
    if self.tokens_code[self.index_token-1] not in set(x[0] for x in self.ensembleNom):
        self.tableDesSymboles.append({"nom": self.tokens_code[self.index_token-1], "classe": classe, "adresse": self.index_token-1})
        self.ensembleNom.add((self.tokens_code[self.index_token-1], self.index_token-1))
    else:
        print("erreur token deja declaré")


def chercherSym(self, token):
    retour = [elt[1] for elt in self.ensembleNom if elt[0] == token]
    if len(retour) != 0: 
        return int(*retour)
    return "ERREUR"