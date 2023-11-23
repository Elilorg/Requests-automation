from selenium import webdriver
import os
from Packagename.constants import URLS
import Packagename.constants as const
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Packagename.actions_de_base import DriverAugmente
from Packagename.externals_functions import Database, creating_pass_and_user_name, random_between


class Bot(DriverAugmente) : 
    def __init__(self, driver_path = const.DRIVER_PATH, teardown=False, likehooman=True, headless = False):
        self.teardown = teardown
        self.driver_path = driver_path
        self.likehooman = likehooman

        super().__init__(headless=headless)
    
    def create_account(self) : 
        password, username = creating_pass_and_user_name()
        self.get(URLS.LANDINGPAGE)

        singup_button = self.find_element(By.CLASS_NAME, "HeaderMenu-link--sign-up")
        singup_button.click()

        mail_input_space = self.find_element(By.ID, "email")
        self.send_keys_like_hooman(mail_input_space, f"{username}@red.fr.cr")

        

        self.click_continue()

        passworld_input = self.find_element(By.ID, "password")
        self.send_keys_like_hooman(passworld_input, password)
    

        self.click_continue(1)

        username_input = self.find_element(By.ID, "login")
        self.send_keys_like_hooman(username_input, username.replace(".", ""))

        self.click_continue(2)

        recieve_news_input = self.find_element(By.NAME, "opt_in")
        self.send_keys_like_hooman(recieve_news_input, "n")
        

        self.click_continue(3)
        

        Database.append({"username" : username, 
        "mail " : f"{username}@red.fr.cr", 
        "password" : password}) 
        





    def click_continue(self, index=0) : 
        time.sleep(random_between())
        continue_button = self.find_elements(By.CLASS_NAME, "js-continue-button")
       
        continue_button[index].click()



    ##IMPLEMENT expected conditions here



    
    

