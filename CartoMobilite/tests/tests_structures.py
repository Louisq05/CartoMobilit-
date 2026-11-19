from structures import *
from collections import deque

print("-------------------SESSION 3--------------------")

# tests pile


pile = []
empiler(pile, "Gare")
empiler(pile, "Parc")
assert sommet(pile) == "Parc"
assert pile == ["Gare", "Parc"]
assert depiler(pile) == "Parc"
assert depiler(pile) == "Gare"
assert pile == []
print("TEST03 : LIFO OK")
pile = []
try:
    depiler(pile)
except IndexError:
    print("TEST03 : dépiler une file vide OK")
print("TEST03 : dépiler une pile vide OK")


file = deque()
enfiler(file, "Gare")
enfiler(file, "Parc")
enfiler(file, "Campus")
assert defiler(file) == "Gare"
assert defiler(file) == "Parc"
assert list(file) == ["Campus"]
print("TEST03 : FIFO OK")

file = deque()
try :
    defiler(file)
except IndexError :
    print("TEST03 : dépiler une file vide OK")


print("------------------------------------------------")
print("TOUS LES TESTS SONT PASSÉS")