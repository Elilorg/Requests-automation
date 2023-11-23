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



class DATABASE():
    name = const.DATABASE_NAME
    
    def get_data(self) : 
        with open(self.name, 'r') as file:
            variable_str = file.read()
            variable = json.loads(variable_str)
        return variable

    def edit_variable(self, variable) : 
        with open(self.name, 'w') as file:
            file.write(json.dumps(variable, indent=4))

    def append(self, value):
        data = self.get_data()
        data += [value]
        self.edit_variable(data)
    
    #### CHECK ###
    def del_last_value(self) : 
        data = open_json_variable(self.name)
        data.pop(-1)
        self.edit_variable(data)
    
    def get_item_number(self, index = 0 ) : 
        data = self.get_data()
        return data[index]
        