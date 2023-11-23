import json
s_part = "DSMDRDFSDLSFMDRDFMRDFTDLFSLMFFSSDD"
partimento = [i for i in s_part]
print(partimento)
with open("./Basses/Basse3.json", "w") as f :
    json.dump(partimento,f)

def reverse_dic(dic) :
    dicte = {}
    for i in dic.keys() : 
        dicte[dic[i]] = i
    return dicte

notes_number = {"D" : 0, "R" : 2,"M": 4, "F":5 ,"S" : 7, "L" : 9, "T" : 11}
notes_degree = {"D" : 1, "R" : 2,"M": 3, "F":4 ,"S" : 5, "L" : 6, "T" : 7}


relation_degre_hauteur_M = [0, 2, 4, 5,7,9,11]
number_notes = reverse_dic(notes_number)
print(f"reverse dicte : {number_notes}")

#degree_note = [None,"D","R","M","F","S","L","S"]

accords_regle_octave_montant = [None,"5","6","6","65","5","6","65","5"]
accords_regle_octave_descendant = [None,"5","6","6","42","5","d6","6","5"]


class Note() : 
    def __init__(self, hauteur = None , note = None) : 
        if not hauteur is None : 
            self.hauteur = hauteur
            self.note =  number_notes[self.hauteur]
        elif note is not None : 
            self.note = note
            self.hauteur = notes_number
            self.degree = ""
        