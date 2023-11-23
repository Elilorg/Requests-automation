from selenium import webdriver
import os
import Packagename.constants as const
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Packagename.actions_de_base import Driver_augmente
from selenium.webdriver.support.ui import Select
from Packagename.externals_functions import creating_pass_and_user_name, sleep_random, bip
import logging
from selenium_recaptcha_solver import RecaptchaSolver



class Bot(Driver_augmente) : 
    def __init__(self, driver_path = const.DRIVER_PATH, teardown=False, likehooman=True, headless = True):

        self.teardown = teardown
        self.driver_path = driver_path
        self.likehooman = likehooman

        self.logger = logging.getLogger("myapp")


        super().__init__(headless=headless, teardown=teardown)



    #### CREER UN COMPTE ####

    def creer_un_compte(self, iteration : int) : 
        self.open_and_switch_tab()
        
        self.get(const.URLS.SING_UP_PAGE)
        
        self.logger.debug("Rejeter les cookies.")
        self.refuse_cookies()
        
        self.logger.info("Création des identifiants")

        name, password = creating_pass_and_user_name()
        
        self.logger.info(str({"name" : name, "email" : f"{name}@yopmail.com", "password" : password}).replace("'", '"'))
    
        self.fill_form(f"{name}@yopmail.com", password, name)

        self.logger.debug("Formulaire complété")

        self.logger.debug("Valider la création du compte")
        valide = self.valider({"name" : name, "email" : f"{name}@yopmail.com", "password" : password})

    
        const.DATABASE().append({"name" : name, "email" : f"{name}@yopmail.com", "password" : password})
        self.logger.debug("Compte ajouté à la base de donnée")

        self.logger.debug("Supression de tout les cookies")
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

        confirm_mail_input = self.find_elements(By.ID, "confirm")
        if len(confirm_mail_input ) > 0 : 
            self.send_keys_like_hooman(confirm_mail_input[0], email)

        password_input = self.find_element(By.ID, "password")
        self.send_keys_like_hooman(password_input, password)

        username_input = self.find_element(By.ID, "displayname")
        self.send_keys_like_hooman(username_input, username)

        day_input = username_input = self.find_element(By.ID, "day")
        self.send_keys_like_hooman(day_input, str(random.randint(1,28)))

        month_input = self.find_element(By.ID, "month")
        select = Select(month_input)
        select.select_by_visible_text("Mars")

        year_input = self.find_element(By.ID, "year")
        year_input.send_keys(str(random.randint(1970, 2000)))

        #gender_input = self.find_element(By.ID, "gender_option_prefernottosay")
        gender_input = self.find_elements(By.CLASS_NAME, "Radio-sc-tr5kfi-0")[-1]
        gender_input.click()

        sing_in_button = self.find_elements(By.CLASS_NAME, "Button-sc-qlcn5g-0")[-1]
        sing_in_button.click()

        return


    
    def valider(self, account) :  
        logger_f_valider = logging.getLogger("valider")
        self.implicitly_wait(5)
        

        capchat = False


        
        if self.current_url == "https://www.spotify.com/fr/signup" : 
            count = 0
            while self.current_url == "https://www.spotify.com/fr/signup" and count < 20 : 
                count +=1 
                time.sleep(0.5)
        
            if count == 20 : 
                raise Exception("Le programme est bloqué sur la page sign up, réessayer.") 
            


        if self.current_url == "https://www.spotify.com/fr/download/windows/" : 
            self.logger.debug("page de téléchargement atteinte, compte crée")
            self.se_connecter(account)
            return True 
        

        
        if "https://challenge.spotify.com/" in self.current_url :  #
            if "dummy" in self.current_url :  #FONCTIONNEL
                self.logger.debug("Créer un compte atteint")
                button_list = self.find_elements(By.CLASS_NAME, "ButtonInner-sc-14ud5tc-0")
                logger_f_valider.info(list(map(lambda x : x.text, button_list)))
                button_list[-1].click()
                input()

            if "recaptcha" in self.current_url : 
                self.logger.warning("RECAPCHAT atteint")
                capchat = True
        


        
        logger_f_valider.debug(self.current_url)


    
        if capchat :
            logger_f_valider.warning("Un Capchat est demandé") 
            capchatframe = self.find_element(By.CSS_SELECTOR, "iframe[title='reCAPTCHA']")
            try : 
                solver = RecaptchaSolver(driver=self)
                solver.click_recaptcha_v2(iframe=capchatframe)
            except Exception as e: 
                logger_f_valider.warning("Erreur du solver")
                logger_f_valider.debug(e)
                raise Exception("Le solveur à beugé, à voir dans les logs du solveur")
            
            logger_f_valider.debug("Capchat résolu")

            button = self.find_elements(By.CLASS_NAME, "ButtonInner-sc-14ud5tc-0")[-1]

            logger_f_valider.debug("Cliquer sur le bouton" + button.text)

            button.click()
            self.se_connecter(account)


           
        


                                            
        
    
    #### SE CONNECTER A UN COMPTE ###

    def se_connecter(self, compte  : dict) : 
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




        

 





    
    

