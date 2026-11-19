pile = []
pile.append("A")
pile.append("B")
pile.append("C")

x = pile.pop()

pile.append("D")

y = pile.pop()

# print("x =", x, "\ny =", y)
# print(pile)

# -------------------------------------------------

# principe de la file en POO

# from collections import deque

class Noeud:
    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant

tete = Noeud("Gare", Noeud("Parc"))
# print(tete.valeur) # Gare
# print(tete.suivant.valeur) # Parc

