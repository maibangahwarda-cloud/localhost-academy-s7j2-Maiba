from pathlib import Path
import json

def charger_taches(chemin): 

 if not Path(chemin).exists(): 
    return []
 else:
   with open("taches.json", "r", encoding="utf8") as f:
    charger_taches = json.load(f)
    return json.load(f)
   isinstance(donne, list)
 return

def sauvegarder_taches(tache, chemin) :
    with open("taches.json", "w", encoding="utf-8") as f:
     json.dump(tache, f, ensure_ascii=False,indent=2)

