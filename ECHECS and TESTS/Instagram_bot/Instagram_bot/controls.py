from selenium import webdriver
import os
import Instagram_bot.constants as const
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Instagram_bot.actions_de_base import Driver_augmente


class Bot(Driver_augmente) : 
    def __init__(self, driver_path = const.DRIVER_PATH, teardown=False, likehooman=True):

        self.teardown = teardown
        self.driver_path = driver_path
        self.likehooman = likehooman

        os.environ['PATH'] += ";" + self.driver_path

        super().__init__()
    
    def accept_cookies(self) : 
        accept_button = self.find_element(By.CLASS_NAME, "_a9--")
        accept_button.click()
    
    def fill_form(self, mail, name, username, passworld) : 
        mail_space = self.find_element(By.NAME, "emailOrPhone")
        self.send_keys_like_hooman(mail_space, mail)

        name_space = self.find_element(By.NAME, "fullName")
        self.send_keys_like_hooman(name_space, name)

        username_space = self.find_element(By.NAME, "username")
        self.send_keys_like_hooman(username_space, username)

        passworld_space = self.find_element(By.NAME, "password")
        self.send_keys_like_hooman(passworld_space, passworld)

        bouton_suivant = list(filter(lambda x : x.text == "Suivant",  self.find_elements(By.CLASS_NAME, "_acan")))[0]
        bouton_suivant.click()


    
    

