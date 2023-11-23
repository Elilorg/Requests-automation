from selenium import webdriver
import os
import Packagename.constants as const
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Packagename.actions_de_base import Driver_augmente
from selenium.webdriver.support.ui import Select
from Packagename.externals_functions import creating_pass_and_user_name, sleep_random, bip, DATABASE
import logging
from selenium_recaptcha_solver import RecaptchaSolver
import requests




class Bot(Driver_augmente) : 
    def __init__(self, driver_path = const.DRIVER_PATH, teardown=True, likehooman=True, headless = True, count=0, _name="BOT", proxy=None, _logger=None):

        self.teardown = teardown
        self.driver_path = driver_path
        self.likehooman = likehooman
        self.headless = headless
        self.reset_needed = False
        self.count = count

        if _logger is None : 
            self.logger = logging.getLogger(str(_name))
            self.logger.setLevel(logging.DEBUG)

            #File handler in the log file
            handler = logging.FileHandler(f"./logs/{_name}.log")
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')     
            handler.setFormatter(formatter) 
            self.logger.addHandler(handler)

            #Console handler used with threading.
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            formatter = logging.Formatter('%(name)s[%(levelname)s] %(message)s')
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

            


        self.error_logger = logging.getLogger("errors")
        
        

        
        
        self._name = _name
        #self.proxy = proxy
        


        super().__init__(headless=headless, teardown=teardown, proxy=proxy)
        self.delete_all_cookies()

    def demarrer(self, limit = 100000) : 
        while not self.reset_needed and self.count<=limit :
            try :  
                self.logger.info(f"Compte numéro {self.count}")
                self.creer_un_compte()
                self.count += 1
            except Exception as e : 
                self.error_logger.critical(str(e))
                if "sign up" in str(e) : 
                    self.error_logger.critical(f"./logs/Errors/{self._name}_{self.count}.png")
                    self.save_screenshot(f"./logs/Errors/{self._name}_{self.count}.png")
                bip()
                self.reset_needed = True
        self.reset()
        return self.demarrer()

        
    
    def reset(self, proxy = None) : 
        self.__exit__(None, None, None)
        self.__init__(driver_path=self.driver_path, 
                      teardown=self.teardown, 
                      headless=self.headless, 
                      count=self.count, _name=self._name)


        ##Trouver un moyen de se régénérer avec nouvelle IP et tout.

    #### CREER UN COMPTE ####

    def creer_un_compte(self) : 
        self.delete_all_cookies()
        self.cycle_tab()
        
        self.get(const.URLS.SING_UP_PAGE)
        
        self.logger.debug("Rejeter les cookies.")
        self.refuse_cookies()
        
        
        name, password = creating_pass_and_user_name()
        
        self.logger.info(str({"name" : name, "email" : f"{name}@yopmail.com", "password" : password}).replace("'", '"'))
    
        self.fill_form(f"{name}@yopmail.com", password, name)

        self.logger.debug("Formulaire cname, password = creating_pass_and_user_name()omplété")

        self.logger.debug("Valider la création du compte")
        valide = self.valider({"name" : name, "email" : f"{name}@yopmail.com", "password" : password})

        database = DATABASE()
        database.append({"name" : name, "email" : f"{name}@yopmail.com", "password" : password, "id" : database.last_id})
        del database
        self.logger.debug("Compte ajouté à la base de donnée")

        self.logger.debug("Supression de tout les cookies")
        time.sleep(3)
        self.delete_all_cookies()
    
    


    def refuse_cookies(self) :
        sleep_random(0.5, 1)
        #self.switch_to.frame(self.find_element(By.NAME, "__tcfapiLocator"))

        refuse_cookies_button = self.find_elements(By.ID, "onetrust-reject-all-handler")
        if len(refuse_cookies_button) == 1 : 
            try : 
                refuse_cookies_button[0].click()
            except : 
                return self.refuse_cookies()
        #self.switch_to.default_content()
        

    def fill_form(self, email, password, username) : 
        mail_input = self.find_element(By.ID, "email")
        self.send_keys_like_hooman(mail_input, email)

        self.implicitly_wait(1)

        confirm_mail_input = self.find_elements(By.ID, "confirm")
        if len(confirm_mail_input ) > 0 : 
            self.send_keys_like_hooman(confirm_mail_input[0], email)
        
        self.implicitly_wait(3)

        password_input = self.find_element(By.ID, "password")
        self.send_keys_like_hooman(password_input, password)

        username_input = self.find_element(By.ID, "displayname")
        self.send_keys_like_hooman(username_input, username)

        day_input = username_input = self.find_element(By.ID, "day")
        self.send_keys_like_hooman(day_input, str(random.randint(1,28)))



        month_input = self.find_element(By.ID, "month")
        select = Select(month_input)
        options = list(map(lambda x : x.text, select.options))[1:]
        self.logger.debug(options)
        select.select_by_visible_text(random.choice(options))

        year_input = self.find_element(By.ID, "year")
        year_input.send_keys(str(random.randint(1970, 2000)))

        #gender_input = self.find_element(By.ID, "gender_option_prefernottosay")
        gender_input = self.find_elements(By.CLASS_NAME, "Radio-sc-tr5kfi-0")[-1]
        gender_input.click()

        sing_in_button = self.find_elements(By.CLASS_NAME, "Button-sc-qlcn5g-0")[-1]
        sing_in_button.click()

        return


    
    def valider(self, account) :  
        self.implicitly_wait(5)
        

        capchat = False


        nb_demi_sec = 40
        if self.current_url == "https://www.spotify.com/fr/signup" : 
            count = 0
            while self.current_url == "https://www.spotify.com/fr/signup" and count < nb_demi_sec : 
                count +=1 
                time.sleep(0.5)
        
            if count == nb_demi_sec : 
                raise Exception(f"{self._name} est bloqué sur la page sign up, réessayer.") 
            

        ### 3 issues possibles : 
        #   1..direct la page telecharger 
        #   2. un bouton créer le compte, à cliquer 
        #   3. un recaptcha

        #1
        if self.current_url == "https://www.spotify.com/fr/download/windows/" or self.current_url == "https://www.spotify.com/fr/download/linux/" :
            self.logger.info("Page de téléchargement atteinte, compte crée")
            return True 
        

        
        if "https://challenge.spotify.com/" in self.current_url :  
            #2
            if "dummy" in self.current_url :  #FONCTIONNEL
                self.logger.info("Créer un compte atteint")
                button_list = self.find_elements(By.CLASS_NAME, "ButtonInner-sc-14ud5tc-0")
                button_list[-1].click()
                return
            #3
            if "recaptcha" in self.current_url : 
                self.logger.warning("RECAPCHAT atteint")
                capchat = True
        


        
        self.logger.debug(self.current_url)


    
        if capchat :
            capchatframe = self.find_element(By.CSS_SELECTOR, "iframe[title='reCAPTCHA']")
            try : 
                solver = RecaptchaSolver(driver=self)
                solver.click_recaptcha_v2(iframe=capchatframe)
            except Exception as e: 
                self.logger.warning("Erreur du solver")
                raise e
            

            button = self.find_elements(By.CLASS_NAME, "ButtonInner-sc-14ud5tc-0")[-1]

            self.logger.debug("Cliquer sur le bouton" + button.text)

            button.click()
            return
        
        self.logger.critical("PAGE INCONNUE")
        self.logger.critical(self.current_url)
        raise Exception(f"Unknown page {self.current_url}")


           
        


                                            
        
    
    #### SE CONNECTER A UN COMPTE ###

    def se_connecter(self, compte  : dict) : 
        """ Connects to a Spotify account using the provided credentials.
        Args: self: The object instance. compte (dict): A dictionary containing email and password keys.
        Returns: None. """

        self.open_and_switch_tab()
        self.get(const.URLS.LOGIN_PAGE)

        if "https://accounts.spotify.com/fr/status" in self.current_url : 
            self.logger.debug("already in")
            return

        username_space = self.find_element(By.ID, "login-username")
        username_space.send_keys(compte["email"])

        password_space = self.find_element(By.ID, "login-password")
        password_space.send_keys(compte["password"])

        login_button = self.find_element(By.ID, "login-button")
        login_button.click()

    
       
    
    def connecter_pour_premium() : 
        pass




        

 





    
    

