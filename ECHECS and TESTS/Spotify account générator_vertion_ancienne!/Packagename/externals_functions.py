import random
from Packagename import constants as const
import json
import time

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

def sleep_random(a = None, b = None ) : 
    if b is None and a is None : 
        raise Exception("Erreur : sleep_random prends au moin un argument.")
        
    if b is None : 
        time.sleep(random.random() * a)
        return
    
    if a > b : 
        raise ValueError("La première valeur doit etre supérieure à la deuxième")
    time.sleep(random.random() * (b-a) + a)
    return

from playsound import playsound
def bip() : 
    playsound('ding.mp3')

    

    