from selenium import webdriver
import os
import Gmail_creator.constants as const
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Gmail(webdriver.Chrome):
    def __init__(self, driver_path=const.webdriver_path, teardown=False, likehooman=False,headless = False):
        #says if we close the browser after we're done
        self.teardown = teardown
        #gives the browser path
        self.driver_path = driver_path
        #sets the driver path
        os.environ['PATH'] += self.driver_path
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'fr'})

        
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
        chrome_options.add_argument("--disable-blink-features")
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_extension("./Gmail_creator/extentions/The-Great-Suspender-Original.crx")
        if headless:
            chrome_options.add_argument("--headless")
        
        
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.0 Safari/537.36'    
        chrome_options.add_argument('user-agent={0}'.format(user_agent))

        
        #On ajoute une extention 
        
        super(Gmail, self).__init__(options=chrome_options)

        #should hide the webdriver property
        self.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        print("exclude navigator.webdriver")


        
        

        self.implicitly_wait(5)
        self.maximize_window()
        self.likehooman = likehooman

    def __exit__(self, exc_type, exc_val, exc_tb):
        a = input()
        if self.teardown:
            time.sleep(2)
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
        self.switch_to.window(self.window_handles[1])
        self.close()
        self.switch_to.window(self.window_handles[0])
        time.sleep(2)
        
    
    def click_on_sing_in(self) :
        buttons = self.find_elements(By.CLASS_NAME , "btn")
        buttons[0].click()
     
        
        
        self.switch_to.window(self.window_handles[-1])
        self.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        
    
    def enter_credentials(self,last_name,username) :
        first_name_form = self.find_element(By.NAME , "firstName")
        self.send_keys_like_hooman(first_name_form, username.split(".")[0])

        last_name_form = self.find_element(By.NAME , "lastName")
        self.send_keys_like_hooman(last_name_form, last_name)

        username_form = self.find_element(By.ID , "username")
        for i in range(12):
            username_form.send_keys(Keys.BACKSPACE)
        self.send_keys_like_hooman(username_form, username)
    
    def enter_passworld(self,password) :
        first_password_form = self.find_element(By.NAME , "Passwd")
        self.send_keys_like_hooman(first_password_form, password)

        second_password_form = self.find_element(By.NAME , "ConfirmPasswd")
        self.send_keys_like_hooman(second_password_form, password)

    def fill_form(self,last_name,username,password) :
        self.enter_credentials(last_name,username)
        self.enter_passworld(password)
    
    def click_next(self) :
        next_button = self.find_element(By.ID , "accountDetailsNext")
        next_button.click()

    def check_antibot(self) :
        self.get("https://bot.sannysoft.com/")


    def send_keys_like_hooman(self, element, keys: str):

        if self.likehooman:
            for i in keys:
                element.send_keys(i)
                time.sleep(random.randint(5, 10) / random.randint(90, 100))
            time.sleep(random.randint(1, 3))
        else:
            element.send_keys(keys)
    



