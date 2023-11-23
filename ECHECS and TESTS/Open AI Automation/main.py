import time
import Packagename.constants as const
from Packagename.constants import URLS
from Packagename.actions_de_base import DriverAugmente
import random 
from Packagename.externals_functions import *
from Packagename.controls import Bot

with Bot(likehooman = False, teardown = False, headless = False) as bot : 
    bot.get(URLS.GOOGLE)
    bot.sing_up()


