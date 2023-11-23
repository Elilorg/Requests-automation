import os
import Packagename.constants as const
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random_user_agent.user_agent import UserAgent
from Packagename.proxylist_scanner.scanners.Hidemyname import HideMyNameScaner
from Packagename.proxylist_scanner.scanner import Portocols, Security
from selenium.webdriver.common.proxy import Proxy, ProxyType
from seleniumwire import webdriver


from webdriver_manager.chrome import ChromeDriverManager

class Driver_augmente(webdriver.Chrome) : 
    def __init__(self, chrome_options = None, headless=False, likehooman=False, teardown=True, proxy = None) : 
        if chrome_options is None :
            chrome_options = webdriver.ChromeOptions()

        capabilities = None
        if proxy is not None : 
            proxy_instance = Proxy()
            proxy_instance.proxy_type = ProxyType.MANUAL
            proxy_instance.http_proxy = proxy
            proxy_instance.ssl_proxy = proxy

            capabilities = webdriver.DesiredCapabilities.CHROME
            proxy_instance.add_to_capabilities(capabilities)



        #dir_path = os.path.abspath('.')s
        #user_dir_path = dir_path + "/.com.google.Chrome.4RNb3y/Default"

        #chrome_options.add_argument(f'user-data-dir={user_dir_path}')


        user_agent = random.choice(const.USER_AGENTS)
        a = """if proxy is None :  #Selenium wire
            
            proxy = "username:password@37.72.141.177:8080"
            options = {"proxy" : {
                "http" : proxy,
                "https" : proxy
            }}"""

            
        chrome_options.add_argument('user-agent={0}'.format(user_agent))
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en-US'})
        chrome_options.add_argument("--lang=en-US")
        chrome_options.add_argument("--disable-extensions")
        
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
    
    def cycle_tab(self) : 
        self.execute_script("window.open('');")
        self.close()
        self.switch_to.window(self.window_handles[-1])
      
    
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
                self.quit()
            
                
    ######### INUTILISES, A REFLECHIR ##########
    def find_and_click(self, selector_type, value) : 
        button = self.find_element(selector_type, value)
        button.click()
    
    def find_and_send_keys(self, selector_type, value, string_to_send) : 
        form = self.find_element(selector_type, value)
        self.send_keys_like_hooman(form, string_to_send)

