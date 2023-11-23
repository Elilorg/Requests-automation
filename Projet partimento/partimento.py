import json

from const import * 
from basse import Basse

basse = Basse(3)
print(basse.notes)
print(basse.trouver_les_possibles_absolus())
basse.visualiser()


#avec basse + Liste des accord on crée les deux voix

