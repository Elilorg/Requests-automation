from Gmail_creator import constants as const
import random 
import json 

def creating_pass_and_user_name():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    numbers = "123456789"
    special_char = "#é/@$!?"
    uppercases = alphabet.upper()

    characters = alphabet + numbers + uppercases
    passworld = [random.choice(characters) for i in range(12)]
    password = "".join(passworld)
    n = random.randint(0, len(const.LISTE) - 1)
    username = const.LISTE[n] + '.' + "".join(
        [random.choice(alphabet) for i in range(random.randint(7, 11))])
    last_name = random.choice(uppercases) + "".join(random.choices(alphabet,k =  random.randint(3,7)))
    return username, last_name, password

def add_account_to_database(name, password) :
    with open(f"./Gmail_creator/{const.database_name}", "r") as f:
        data = json.load(f)
    print(data)
    data.append({"name" : name, "password" : password})
    print(data)
    with open(f"./Gmail_creator/{const.database_name}","w") as f :
        json.dump(data,f)

def substract_last_account() :
    with open(f"./Gmail_creator/{const.database_name}", "r") as f:
        data = json.load(f)
    print(data)
    data.pop(-1)
    print(data)
    with open(f"./Gmail_creator/{const.database_name}","w") as f :
        json.dump(data,f)