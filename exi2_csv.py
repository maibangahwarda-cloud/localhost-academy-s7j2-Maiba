taches = [
{" titre ": " Reviser Python ", " faite ": False } ,
{" titre ": " Lire le cours ", " faite ": True } ,
{" titre ": " Acheter du pain , du lait ", " faite ": False }
]

import csv
with open("taches.csv", "w", newline="",encoding="utf8") as fichier:
    writer = csv.DictWriter(
fichier, fieldnames=["titre", "faite"]
)
    writer.writeheader()
    writer.writerow("tache")

importer_csv(chemin)

