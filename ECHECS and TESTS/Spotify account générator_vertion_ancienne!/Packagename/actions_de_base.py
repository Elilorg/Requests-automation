from selenium import webdriver
import os
import Packagename.constants as const
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

class Driver_augmente(webdriver.Chrome) : 
    def __init__(self, chrome_options = None, headless=False, likehooman=False, teardown=False) : 
        if chrome_options is None :
            chrome_options = webdriver.ChromeOptions()

        

        user_agent = random.choice([  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4083.0 Safari/537.36",  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"])
  
        chrome_options.add_argument('user-agent={0}'.format(user_agent))
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'fr'})

        
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
        chrome_options.add_argument("--disable-blink-features")
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--window-size=1920x1080")

        #chrome_options.add_extension('extentions/extension_2_0_1_0.crx')
        #chrome_options.add_extension("extentions/CRX-Extractor-Downloader.crx")
        #chrome_options.add_extension("extentions/TestCase-Studio.crx")
        #chrome_options.add_extension("extentions/SelectorsHub.crx")
        if headless : 
            chrome_options.add_argument("--headless")
        
        
        super().__init__(ChromeDriverManager().install(), chrome_options=chrome_options)
        
        self.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        

        self.implicitly_wait(3)
        self.maximize_window()
        
        self.likehooman = likehooman
        self.teardown = teardown
    
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
            
            time.sleep(2)
            if self.teardown:
                self.quit()
            else : 
                a=input("Valider la sortie")
            
                
    ######### INUTILISES, A REFLECHIR ##########
    def find_and_click(self, selector_type, value) : 
        button = self.find_element(selector_type, value)
        button.click()
    
    def find_and_send_keys(self, selector_type, value, string_to_send) : 
        form = self.find_element(selector_type, value)
        self.send_keys_like_hooman(form, string_to_send)

