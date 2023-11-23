import json

def reverse_dic(dic) :
    dicte = {}
    for i in dic.keys() : 
        dicte[dic[i]] = i
    return dicte


notes_number = {"D" : 0, "R" : 2,"M": 4, "F":5 ,"S" : 7, "L" : 9, "T" : 11}
notes_degree = {"D" : 1, "R" : 2,"M": 3, "F":4 ,"S" : 5, "L" : 6, "T" : 7}


relation_degre_hauteur_M = [0, 2, 4, 5,7,9,11]
number_notes = reverse_dic(notes_number)

accords_regle_octave_montant = [None,"5","6","6","65","5","6","65","5"]
accords_regle_octave_descendant = [None,"5","6","6","42","5","d6","6","5"]

degres_accords = {"5" : (0,2,4), "6" : (2,0,5), "65" : (5,4,2), "64" : (3,5), "54" : (3,4),"42" : (1,3,5),"d6" : (2,0,6)}


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