def PRN(self):
    print(self.pile.pop())
    self.pointeur_instruction += 1


def INN(self):
    try:
        self.pile[self.pile[-1]] = int(input())
        self.pointeur_instruction += 1
    except ValueError:
        print("ERREUR dans l'entrée, doit etre convertible en int")
        import sys
        sys.exit()
