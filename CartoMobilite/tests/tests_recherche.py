from catalogue import *

stations = charger_stations("../data/stations.csv")
assert [s["id"] for s in rechercher_nom(stations, "parc")] == ["S04"]
print("TEST04 : cas nominal OK")
assert [s["id"] for s in rechercher_nom(stations, "gaRe")] == ["S01"]
print("TEST04 : insensibilité à la casse OK")
assert rechercher_nom(stations, "xyz") == []
print("TEST04 : recherche d'un élément non compris OK")
