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
    return sum(nom.startswith(motif) for nom in noms)

def charger_arrets(chemin: str = "/home/louis/Python/CartoMobilite/data/arrets_l5_l8") -> list[str]:
    with open(chemin, encoding="utf-8") as f:
        return [ligne.strip() for ligne in f if ligne.strip()]

