import time
import Instagram_bot.constants as const
from Instagram_bot.actions_de_base import Driver_augmente
import random 
from Instagram_bot.externals_functions import *
from Instagram_bot.controls import Bot

with Bot() as bot : 
    bot.land("Instagram_account_creation")
    bot.accept_cookies()
    bot.fill_form("mail", "name", "username", "passworld")
