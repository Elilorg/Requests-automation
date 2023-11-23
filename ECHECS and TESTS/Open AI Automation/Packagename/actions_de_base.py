from selenium import webdriver
import os
import Packagename.constants as const
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

class DriverAugmente(webdriver.Chrome) : 
    def __init__(self, chrome_options = None, headless=False, teardown=False) : 
        if chrome_options is None :
            chrome_options = webdriver.ChromeOptions()

        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'    
        chrome_options.add_argument('user-agent={0}'.format(user_agent))
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'fr'})

        
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
        chrome_options.add_argument("--disable-blink-features")
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--window-size=1920x1080")

        if headless : 
            chrome_options.add_argument("--headless")
        
        
        super().__init__(ChromeDriverManager().install(), chrome_options=chrome_options)
        
        self.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        

        self.implicitly_wait(15)
        self.maximize_window()
        
    def land(self, keyworld) : 
        self.get(const.URLS[keyworld])
    
    def open_and_switch_tab(self):
        self.execute_script("window.open('');")
        self.switch_to.window(self.window_handles[-1])
        time.sleep(1)
    
    def send_keys_like_hooman(self, element, keys: str):
        if self.likehooman:
            for i in keys:
                element.send_keys(i)
                time.sleep((random.random() * 0.2) + 0.1)
            time.sleep((random.random() * 1) + 1)
        else:
            element.send_keys(keys)
    
    def __exit__(self, exc_type, exc_val, exc_tb):
            a = input(">>>entrez pour terminer")
            time.sleep(2)
            if self.teardown:
                self.quit()
            else : 
                a = input()
                
    ######### INUTILISES, A REFLECHIR ##########
    def find_and_click(selector_type, value) : 
        button = self.find_element(selector_type, value)
        button.click()
    
    def find_and_send_keys(selector_type, value, string_to_send) : 
        form = self.find_element(selector_type, value)
        self.send_keys_like_hooman(form, string_to_send)
