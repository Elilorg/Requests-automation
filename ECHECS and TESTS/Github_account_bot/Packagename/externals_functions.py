import random
from Packagename import constants as const
import json
import openpyxl

def creating_pass_and_user_name():
    character = 'abcdefghijklmnopqrstuvwxyz1234567890AZERTYUIOPQSDFGHJKLMWXCVBN'
    passworld = [random.choice(character) for i in range(12)]
    password = "".join(passworld)
    print(password)
    n = random.randint(0, len(const.LISTE) - 1)
    name = const.LISTE[n] + '.' + "".join(
        [random.choice(character) for i in range(random.randint(6, 9))])
    return name, password



class Database():
    name = const.DATABASE_NAME
    
    def get_data() : 
        with open(Database.name, 'r') as file:
            variable_str = file.read()
            variable = json.loads(variable_str)
        return variable

    def edit_variable( variable) : 
        with open(Database.name, 'w') as file:
            file.write(json.dumps(variable, indent=4))

    def append( value):
        data = Database.get_data()
        data += [value]
        Database.edit_variable(data)
    
    #### CHECK ###
    def del_last_value() : 
        data = open_json_variable(Database.name)
        data.pop(-1)
        Database.edit_variable(data)
    
    def get_item_number( index = 0 ) : 
        data = Database.get_data()
        return data[index]
        

def random_between(a=1, b=2) : 
    return a + random.random() * (b-a)
