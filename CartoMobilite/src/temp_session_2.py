stations = [
{"id": "S01", "nom": "Gare", "zone": "1"},
{"id": "S02", "nom": "Hôtel de Ville", "zone": "1"},
{"id": "S03", "nom": "Université", "zone": "2"}
]

# _______Cours____________

# for station in stations :
#     print(station["id"], station["nom"])

# ________EX1_____________

# print(stations[1]["nom"]) # Print le nom associé à l'élément d'index 1 dans le dictionnaire : "Hôtel de Ville"

# ________EX2____________

# for station in stations :
#     print(station["id"])

# _______EX3______________

# la structure de donnée qui garanti l'unicité (ou l'absence de doublons) est le set

# ________EX4_____________

# stations_test = [
# {"id": "S01", "nom": "Gare", "zone": "1"},
# {"id": "S01", "nom": "Hôtel de Ville", "zone": "1"},
# {"id": "S01", "nom": "Université", "zone": "2"}
# ]
# for station in stations_test :
#    print(station["id"], station["nom"])

# Pas d'erreur, deux records sont créés car les doublons sont autorisés.