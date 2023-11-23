import time
import Packagename.constants as const
from Packagename.actions_de_base import DriverAugmente
import random 
from Packagename.externals_functions import *
from Packagename.controls import Bot

with Bot(likehooman = True, teardown = False, headless = False) as bot : 

    bot.create_account()
    pass
