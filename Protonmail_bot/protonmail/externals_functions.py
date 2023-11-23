import json
import random
import time
from protonmail import constants as const


def open_json_variable(filename):
    with open(filename, 'r') as file:
        variable_str = file.read()
        variable = json.loads(variable_str)

    return variable


def edit_json_variable(variable, filename):
    with open(filename, 'w') as file:
        file.write(json.dumps(variable, indent=4))


def creating_pass_and_user_name():
    character = 'abcdefghijklmnopqrstuvwxyz1234567890AZERTYUIOPQSDFGHJKLMWXCVBN'
    passworld = [random.choice(character) for i in range(12)]
    password = "".join(passworld)
    print(password)
    n = random.randint(0, len(const.LISTE) - 1)
    name = const.LISTE[n] + '.' + "".join(
        [random.choice(character) for i in range(random.randint(6, 9))])
    return name, password
