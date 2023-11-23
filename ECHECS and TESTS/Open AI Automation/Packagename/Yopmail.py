from selenium import webdriver
import os
import Packagename.constants as const
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Packagename.actions_de_base import DriverAugmente
from Packagename.constants import URLS

class YopmailBot() : 
    ##################  YOPMAIL  ####################

    def enter_yopmail_page_and_grab_code(self, adress="elias"):
        self.open_and_switch_tab()
        self.get(URLS.YOPMAIL)
        self.click_for_cookies_or_pass()
        self.enter_random_adress(adress)
        code = self.read_verification_code()
        return code
    
    def click_for_cookies_or_pass(self):
        skip_cookies = self.find_elements(By.ID, "necesary")
        if not len(skip_cookies) == 0:
            skip_cookies[0].click()

    def enter_random_adress(self, adress="elias"):
        adress_space = self.find_element(By.ID, "login")
        print(adress_space)
        for i in range(12):
            adress_space.send_keys(Keys.DELETE)
        self.send_keys_like_hooman(adress_space, adress)
        adress_space.send_keys(Keys.ENTER)

    

    def read_verification_code(self):
        link_texts = []
        while True : 
            try : 
                frame = self.find_element(By.ID, "ifmail")
            except : 
                time.sleep(1)
                print("Waiting")
        self.switch_to.frame(frame)

        while "Verify email address" not in link_texts : 
            
            buttons = self.find_elements(By.TAG_NAME, "a")
            link_texts = [i.text for i in buttons]
            print(link_texts)
        
            
        
        link = buttons[0].href
        print(link)
        link.click()
        self.switch_to.default_content()
        return 
    
    #Cherche le code et ne le renvoie que si c bon 
    def search_code(self) :
        pass