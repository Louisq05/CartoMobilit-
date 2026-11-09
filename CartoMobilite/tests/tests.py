from catalogue import *
from pathlib import Path

liste_arrets = charger_arrets()
liste_vide = []

print("---------------------------------------------------------")

# Tests fonction compter_stations()
assert(compter_stations(liste_vide, "De Musset", True)) == 0
print("TEST : compter_stations, ensemble vide OK")
assert(compter_stations(liste_arrets, "de musset", True)) == 0
print("TEST : compter_stations, sensible casse OK")
assert(compter_stations(liste_arrets, "de musset", False)) == 2
print("TEST : compter_stations, insensible casse OK")
assert(compter_stations(liste_arrets, "de mussetttttttttttttttttttttttttttttttt", False)) == 0
print("TEST : compter_stations, prefix trop long OK")

print("---------------------------------------------------------")

# Tests fonction filtrer_stations()
assert(filtrer_stations(liste_vide, "De Musset", True)) == 0
print("TEST : filtrer_stations, ensemble vide OK")
assert(filtrer_stations(liste_arrets, "de musset", True)) == 0
print("TEST : filtrer_stations, sensible casse OK")
assert(filtrer_stations(liste_arrets, "de musset", False)) == 2
print("TEST : filtrer_stations, insensible casse OK")
assert(filtrer_stations(liste_arrets, "de mussettttttttttttttttttttttttttttttttttt", False)) == 0
print("TEST : filtrer_stations, motif top long OK")

print("---------------------------------------------------------")
