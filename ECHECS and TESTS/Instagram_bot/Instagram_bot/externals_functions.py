from Instagram_bot.constants import const

def generate_passworld() : 
    passworld = ""
    for i in range(10) : 
        passworld += random.choice(const.PASSWORLD_CHARACTERS)
    return passworld

    

