import json
from const import *

#Fonction qui retourne les notes autorisée (a,b,c)

#Fonction qui évalue le score dde chaque couple de deux notes (aa,ab,ba,ac,bc)

def load_bass(number : int) : 
    with open(f"./Basses/Basse{number}.json","r") as f :
        return json.load(f)

def trad_number(basse : list) : 
    trad = []
    for i in basse : 
        trad.append(notes_number[i])
    return trad

def trad_degree(basse : list) :
    trad = []
    for i in basse : 
        trad.append(notes_degree[i])
    return trad 

class Basse() :
    def __init__(self,nb : int) :
        self.notes = load_bass(nb)
        self.hauteur = trad_number(self.notes)
        self.degres = trad_degree(self.notes)
        self.longueur = len(self.notes)
        self.chiffrer()

        #Créer une liste des accords à partir de la basse
    def chiffrer(self) : 
        accords = [None for i in range(len(self.notes))]
        degres_basse = self.degres
        for index, degre in enumerate(degres_basse) :
            if accords[index] is None :
                #Si on est sur le deg 5 et qu'on est pas a la fin
                if degre ==  5 and index < len(degres_basse)-1: 
                    # Si on a deux 5 de suite 
                    if degres_basse[index+1] == 5 and degres_basse[index+2] != 5 :
                        #Cadenza composta
                        accords[index] = "64"
                        accords[index+1] = "5"
                    elif degres_basse[index+1] == 5 and degres_basse[index+2] == 5 and degres_basse[index+3] == 5 and degres_basse[index+4] != 5  :
                        #Cadenza doppia
                        accords[index] = "5"
                        accords[index+1] = "64"
                        accords[index+2] = "54"
                        accords[index+3] = "5"
                    else : 
                        #Sol dans le cadre de la regle de l'octave
                        accords[index] = "5"
                #Regle de l'octave    
                else : 
                    if index < len(degres_basse)-1 : 
                    #On check si ca monte ou descend 
                        if degres_basse[index+1] - degre >= 0 or degres_basse[index+1] - degre == -6: 
                            #Ca monte ou egal : regle montante 
                            accords[index] = accords_regle_octave_montant[degre]
                        else : 
                            accords[index] = accords_regle_octave_descendant[degre]
                            #Ca descend : regle descendante 
                    else : 
                        accords[index] = "5"
        self.accords = accords
        return accords
    
    def trouver_les_possibles_absolus(self) : 
        possibles_absoulus = [[] for i in range(self.longueur)]
        for index, id_accord in enumerate(self.accords) :
            nb_octaves = 1
            for octave in range(nb_octaves) : 
                for i in degres_accords[id_accord] : 
                    degre_de_la_note = self.degres[index] + i + 7*octave
                    hauteur_de_la_note = relation_degre_hauteur_M[(degre_de_la_note-1)%7]
                    possibles_absoulus[index].append(number_notes[hauteur_de_la_note])

        #Convertir les degres en hauteur absolue
        
        return possibles_absoulus
   

    def realisation(self) : 
        self.trouver_les_possibles_absolus()


    def visualiser(self) :
        espace_entre_les_notes = 4
        lignes = [[ " " for i in range(self.longueur* espace_entre_les_notes) ] for i in range(11)]
        #On transforme une ligne sur 2 en veritable ligne
        for i in range(0,11,2) :
            lignes[i] = ["-" for i in range(espace_entre_les_notes * self.longueur)]
        lignes[10] = [" " for i in range(self.longueur*espace_entre_les_notes) ]
        for ligne_note in notes_degree.keys() :
            for index, note in enumerate(self.notes) :  
                if note == ligne_note : 
                    lignes[notes_degree[ligne_note]+2][index * espace_entre_les_notes] = "¤"
        
        #J'imprime les lignes à l"envers 
        for i in lignes[::-1] : print("".join(i))

        


basse = Basse(3)
print(basse.notes)
print(basse.trouver_les_possibles_absolus())
basse.visualiser()

