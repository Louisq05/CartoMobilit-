from catalogue import *
from pathlib import Path

def leve_value_error(fonction, *args) -> bool:
    """True si fonction(*args) lève une ValueError, False sinon."""
    try:
        fonction(*args)
    except ValueError:
        return True
    return False

liste_arrets = charger_arrets()
liste_vide = []

print("-------------------SESSION 1--------------------")

# tests fonction compter_stations()
assert compter_stations(liste_vide, "De Musset", True) == 0
print("TEST01 : compter_stations, ensemble vide OK")
assert compter_stations(liste_arrets, "de musset", True) == 0
print("TEST01 : compter_stations, sensible casse OK")
assert compter_stations(liste_arrets, "de musset", False) == 2
print("TEST01 : compter_stations, insensible casse OK")
assert compter_stations(liste_arrets, "de mussetttttttttttttttttttttttttttttttt", False) == 0
print("TEST01 : compter_stations, prefixe trop long OK")

print("---------------------------------------------------------")

# tests fonction filtrer_stations()
assert filtrer_stations(liste_vide, "De Musset", True) == 0
print("TEST01 : filtrer_stations, ensemble vide OK")
assert filtrer_stations(liste_arrets, "de musset", True) == 0
print("TEST01 : filtrer_stations, sensible casse OK")
assert filtrer_stations(liste_arrets, "de musset", False) == 2
print("TEST01 : filtrer_stations, insensible casse OK")
assert filtrer_stations(liste_arrets, "de mussettttttttttttttttttttttttttttttttttt", False) == 0
print("TEST01 : filtrer_stations, motif trop long OK")

print("---------------------SESSION 2-------------------")

RACINE = Path(__file__).resolve().parents[1]
DATA = RACINE / "data"

# tests fonction charger_stations
stations = charger_stations(DATA / "stations.csv")
assert len(stations) == 14
print("TEST02 : charger_stations, cas nominal (14 stations) OK")
assert stations[0]["id"] == "S01"
assert stations[2]["nom"] == "Université"
print("TEST02 : charger_stations, contenu OK")
assert all(set(s.keys()) == {"id", "nom", "zone"} for s in stations)
print("TEST02 : charger_stations, colonnes id/nom/zone OK")

assert leve_value_error(charger_stations, DATA / "stations_sans_id.csv")
print("TEST02 : charger_stations, colonnes obligatoires -> ValueError OK")
assert leve_value_error(charger_stations, DATA / "stations_id_vide.csv")
print("TEST02 : charger_stations, id vide -> ValueError OK")
assert leve_value_error(charger_stations, DATA / "stations_doublon_id.csv")
print("TEST02 : charger_stations, doublon d'id -> ValueError OK")

print("---------------------------------------------------------")

# tests fonction index_par_id
index = index_par_id(stations)
assert index["S03"]["nom"] == "Université"
print("TEST02 : index_par_id, S03 = Université OK")
assert index["S14"]["nom"] == "Jardin botanique"
assert index["S14"]["zone"] == "4"
print("TEST02 : index_par_id, S14 = Jardin botanique, zone 4 OK")
assert "S99" not in index and index.get("S99") is None
print("TEST02 : index_par_id, identifiant absent OK")

doublons = [{"id": "S01", "nom": "A", "zone": "1"},
            {"id": "S01", "nom": "B", "zone": "2"}]
assert leve_value_error(index_par_id, doublons)
print("TEST02 : index_par_id, doublon d'id -> ValueError OK")

print("---------------------------------------------------------")

# tests fonction zones_uniques
assert zones_uniques(stations) == {"1", "2", "3", "4"}
print("TEST02 : zones_uniques, 4 zones distinctes OK")
assert zones_uniques(doublons) == {"1", "2"}
print("TEST02 : zones_uniques, doublons de zones éliminés OK")

















print("---------------------------------------------------------")
print("TOUS LES TESTS SONT PASSÉS")