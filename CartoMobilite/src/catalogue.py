import csv

def compter_stations(noms: list[str] | None, prefixe: str | None, casse: bool = True) -> int:
    if not noms or prefixe is None or len(prefixe) > 10 or len(noms) > 100 :
        return 0
    if not casse:
        prefixe = prefixe.lower()
        return sum(nom.lower().startswith(prefixe) for nom in noms)
    return sum(nom.startswith(prefixe) for nom in noms)

def filtrer_stations(noms: list[str] | None, motif: str | None, casse: bool = True) -> int:
    if not noms or motif is None or len(motif) > 10 or len(noms) > 100:
        return 0
    if not casse:
        motif = motif.lower()
        return sum(motif in nom.lower() for nom in noms)
    return sum(motif in nom for nom in noms)  # corrigé : startswith -> in

def charger_arrets(chemin: str = "/home/louis/Documents/Python/CartoMobilite/data/arrets_l5_l8") -> list[str]:
    with open(chemin, encoding="utf-8") as f:
        return [ligne.strip() for ligne in f if ligne.strip()]

def charger_stations(path) -> list[dict]:
    with open(path,  # ouverture du csv
              encoding="utf-8",
              newline="") as f:
        lecteur = csv.DictReader(f)  # création dict
        colonnes = lecteur.fieldnames or []

        # vérif présence des colonnes obligatoires
        manquantes = {"id", "nom", "zone"} - set(colonnes)
        if manquantes:
            raise ValueError(f"Colonnes manquantes : {sorted(manquantes)}")

        stations = list(lecteur)  # liste de dict

    ids_vus = set()
    for station in stations:
        if not station["id"] or not station["id"].strip():
            raise ValueError("Identifiant vide")
        if station["id"] in ids_vus:
            raise ValueError(f"Identifiant dupliqué : {station['id']}")
        ids_vus.add(station["id"])

    return stations

def index_par_id(stations: list[dict]) -> dict[str, dict]:
    index = {}
    for station in stations:
        code = station["id"]
        if code in index:
            raise ValueError(f"Identifiant dupliqué : {code}")
        index[code] = station  # station complète, pas {nom: zone}
    return index

def zones_uniques(stations) -> set[str]:
    zones = set()
    for station in stations:
        zones.add(station["zone"])  # zones gardées en chaînes (contrat du projet)
    return zones