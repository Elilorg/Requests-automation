
import time
import Packagename.constants as const
from Packagename.actions_de_base import Driver_augmente
import random 
from Packagename.externals_functions import *
from Packagename.controls import Bot
import logging


import logging
import sys

print(sys.argv)
if "--headless" == sys.argv[1] : 
    headless = True
else : headless = False

valider_log_level = logging.DEBUG
app_log_level = logging.DEBUG


logging.basicConfig(level=logging.WARNING)


logger = logging.getLogger("myapp")
logger.setLevel(app_log_level)


# Create a handler to write logs to a file
handler = logging.FileHandler("./logs/myapp.log")
handler.setLevel(app_log_level)


# Create a formatter to format the log messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)


# Add the handler to the logger
logger.addHandler(handler)

# Set propagate to False for all the handlers of the root logger
logging.getLogger().handlers[0].propagate = False



logger_f_valider = logging.getLogger("valider")
logger_f_valider.setLevel(valider_log_level)

valider_handeler = logging.FileHandler("./logs/valider.log")
valider_handeler.setLevel(valider_log_level)

valider_handeler.setFormatter(formatter)
logger_f_valider.addHandler(valider_handeler)







account = 0
error_count = 0
while account < 400 : 
    with Bot(likehooman = False, teardown = True, headless = headless) as bot : 
        
        for i in range(10) : 
            print()       
            logger.info("Compte n" + str(account))
     
            try : 
                bot.creer_un_compte(i)
                account +=1
                
            


            except Exception as e:
                logger.debug("ERRUEUR DANS CREER COMPTE")
                logger.debug(e)
                bip()
                input()
                
                error_count += 1
                break
                

            logger.debug("NB erreurs : " + str(error_count))
            
            
    


