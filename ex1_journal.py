from pathlib import Path
chemin = Path("journal.txt")

if not chemin.exists():
   with chemin.open("w", encoding="utf8") as fichier:
    for i in range(3):
     titre = input(f"mettre le titre{i + 1} : ")
     fichier.write(titre + "\n")
else :
  titre = input(f"ajouter un autre titre:")
  with chemin.open("a", encoding="utf8") as fichier:
   fichier.append(titre +"\n")

with chemin.open("r", encoding="utf8") as fichier:
  contenu = fichier.reader()
  
 #e mode W permet de créer une tache mais écrase l'encienne si elle existait.
#le mode a ajoute une tache à la fin. r ouvre la lecture