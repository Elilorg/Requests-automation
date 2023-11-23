from selenium import webdriver
import os
import Packagename.constants as const
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Packagename.actions_de_base import DriverAugmente
from Packagename.Yopmail import YopmailBot


class Bot(DriverAugmente, YopmailBot) : 
    def __init__(self, driver_path = const.DRIVER_PATH, teardown=False, likehooman=True, headless = False):
        self.teardown = teardown
        self.driver_path = driver_path
        self.likehooman = likehooman

        
        super().__init__(headless=headless)
    
    def sing_up(self) :
        email = f"email{random.randint(10, 99)}@yopmail.com"

        link_to_click = self.find_elements(By.CLASS_NAME, "QS5gu") 
        link_to_click[2].click()

        link_to_click = self.find_element(By.CLASS_NAME, "LC20lb") 
        link_to_click.click()

        email_form = self.find_element(By.ID, "email")
        self.send_keys_like_hooman(email_form, email)

        self.click_continue()
        
        while True : 
            try : 
                password_form = self.find_element(By.ID, "password")
                break
            except : 
                time.sleep(0.5)
                print("waiting...")
                pass
        
        self.send_keys_like_hooman(password_form, "MyPassword")

        self.click_continue()

        self.verify_email(email)

        inputs = self.find_elements(By.CLASS_NAME, "")


    def click_continue(self) : 
        button = self.find_element(By.NAME, "action")
        button.click()

    def verify_email(self, email) :
        code = self.enter_yopmail_page_and_grab_code(adress=email)




    
    

