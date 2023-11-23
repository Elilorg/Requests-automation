import random
from Packagename import constants as const
import json
import time
from Packagename.constants import DATABASE_NAME
import types

def creating_pass_and_user_name():
    character = 'abcdefghijklmnopqrstuvwxyz1234567890AZERTYUIOPQSDFGHJKLMWXCVBN'
    passworld = [random.choice(character) for i in range(12)]
    password = "".join(passworld)
    print(password)
    n = random.randint(0, len(const.LISTE) - 1)
    name = const.LISTE[n] + '.' + "".join(
        [random.choice(character) for i in range(random.randint(6, 9))])
    return name, password

def open_json_variable(filename):
    with open(filename, 'r') as file:
        variable_str = file.read()
        variable = json.loads(variable_str)

    return variable


def edit_json_variable(variable, filename):
    with open(filename, 'w') as file:
        file.write(json.dumps(variable, indent=4))



class DATABASE() : 
    name = DATABASE_NAME
    def append(self, value) : 
        data = self.open_file()
        data += [value]
        self.edit_file(data)
    
    @property
    def last_id(self) : 
        data = open_json_variable(self.name)
        last_id = len(data) - 1
        return last_id
    
    def open_file(self) : 
        with open(self.name, 'r') as file:
            variable_str = file.read()
            variable = json.loads(variable_str)

        return variable
    
    
    def edit_file(self, data : list[dict] ) :
        if not (isinstance(data, dict) or isinstance(data, list)) :
            raise TypeError("Seulement dict et listes dans un fichier json") 
        with open(self.name, 'w') as file:
            file.write(json.dumps(data, indent=4))
    

    

def sleep_random(a = None, b = None ) : 
    if b is None and a is None : 
        raise TypeError("Erreur : sleep_random prends au moin un argument.")
        
    if b is None : 
        time.sleep(random.random() * a)
        return
    
    if a > b : 
        raise ValueError("La première valeur doit etre supérieure à la deuxième")
    time.sleep(random.random() * (b-a) + a)
    return

from playsound import playsound
def bip() : 
    playsound('./sounds/ding.mp3')

    

    