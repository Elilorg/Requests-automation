from protonmail.proton import Proton
import time
import random
import json
from protonmail import constants as const
from xlsx_convert import xml_add
from protonmail.externals_functions import *


# ouvrir les donées du fichier des comptes
accounts = open_json_variable('accounts.json')



def create_an_account():
    with Proton(teardown=False, likehooman=False) as bot:
        account = bot.create_account()
        xml_add(account)
        
def create_n_account(n) : 
    with Proton(teardown=False, likehooman=False) as bot:
        for i in range(n) : 
            account = bot.create_account()
            
            xml_add(account)


def connect_to_the_account(number=0):
    account = open_json_variable('accounts.json')[number]
    with Proton(teardown=False, likehooman=False) as bot:
        bot.connect_to(account)
        


def connect_to_every_accounts():
    accounts = open_json_variable('accounts.json')
    with Proton(teardown=False, likehooman=False) as bot:
        for account in accounts:
            bot.open_and_switch_tab()
            bot.connect_to(account) 

create_n_account(2)