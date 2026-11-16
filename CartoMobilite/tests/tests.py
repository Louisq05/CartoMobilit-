from catalogue import *
from pathlib import Path

liste_arrets = charger_arrets()
liste_vide = []

print("-------------------SESSION 1--------------------")

# tests fonction compter_stations()
assert(compter_stations(liste_vide, "De Musset", True)) == 0
print("TEST01 : compter_stations, ensemble vide OK")
assert(compter_stations(liste_arrets, "de musset", True)) == 0
print("TEST01 : compter_stations, sensible casse OK")
assert(compter_stations(liste_arrets, "de musset", False)) == 2
print("TEST01 : compter_stations, insensible casse OK")
assert(compter_stations(liste_arrets, "de mussetttttttttttttttttttttttttttttttt", False)) == 0
print("TEST01 : compter_stations, prefix trop long OK")

print("---------------------------------------------------------")

# tests fonction filtrer_stations()
assert(filtrer_stations(liste_vide, "De Musset", True)) == 0
print("TEST01 : filtrer_stations, ensemble vide OK")
assert(filtrer_stations(liste_arrets, "de musset", True)) == 0
print("TEST01 : filtrer_stations, sensible casse OK")
assert(filtrer_stations(liste_arrets, "de musset", False)) == 2
print("TEST01 : filtrer_stations, insensible casse OK")
assert(filtrer_stations(liste_arrets, "de mussettttttttttttttttttttttttttttttttttt", False)) == 0
print("TEST01 : filtrer_stations, motif top long OK")

print("---------------------SESSION 2-------------------")

# tests fonction charger_stations
RACINE = Path(__file__).resolve().parents[1]
CHEMIN = RACINE / "data" / "stations.csv"
assert(charger_stations(CHEMIN) != None)
print("TEST02 : cas nominal OK")

CHEMIN = RACINE / "data" / "stations_sans_id.csv"
assert(charger_stations(CHEMIN) == None)
print("TEST02 : colonnes obligatoires OK")

CHEMIN = RACINE / "data" / "stations_id_vide.csv"
assert(charger_stations(CHEMIN) == None)
print("TEST02 : id vide OK")

CHEMIN = RACINE / "data" / "stations_doublon_id.csv"
assert(charger_stations(CHEMIN) == None)
print("TEST02 : doublon d'id OK")

# tests fonction index_par_id
CHEMIN = RACINE / "data" / "stations_doublon_id.csv"
assert(index_par_id(charger_stations(CHEMIN)) == None)
print("TEST02 : doublon d'id 02 OK")
