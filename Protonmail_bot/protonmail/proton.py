
from selenium import webdriver
import os
import protonmail.constants as const
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from protonmail.actions_de_base import DriverAugmente
from protonmail.externals_functions import *



class Proton(DriverAugmente):
    def __init__(self, driver_path = const.DRIVER_PATH, teardown=False, likehooman=True):

        self.teardown = teardown
        self.driver_path = driver_path
        os.environ['PATH'] += ";" + self.driver_path
        super().__init__()
        self.likehooman = likehooman



######### CREEER UN COMPTE ######## (depth 0)
    def create_account(self) : 
            name, passworld = creating_pass_and_user_name()
            self.open_and_switch_tab()

            print(str({"name" : name, "passworld" : passworld}).replace("'", '"'))

            self.land("Proton_create")
            self.fill_form(name, passworld)
            self.enter_verification_email(name.split('.')[0] + '@nabi.ml')
            time.sleep(random.random()*2 + 1)
            code = self.enter_yopmail_page_and_grab_code(name.split('.')[0])
            print(code)
            self.close_tab_and_enter_code(code)
            print("ACCOUNT CREATED")
            return {"name" : name, "passworld" : passworld}

 


##################### CREATION OF THE ACCOUNT #####################

    def fill_form(self, name, password): #(depth 1)
        self.enter_username(name)
        self.enter_passworld_and_verification(password)
        self.click_on_next_button()
        self.click_free_button()


    def enter_username(self, username='Yan.barthe'):  #(depth 2)
        self.switch_to.frame(self.find_element(
            By.CLASS_NAME, "challenge-width-increase"))  # l'element que je cherche est
        # contenu dans une iframe
        # je switche d'abbord de frame puis je trouve l'élément dans
        # la frame
        username_space = self.find_element(By.ID, 'email')
        # remplissage de l'adresse mail
        self.send_keys_like_hooman(username_space, username)
        self.switch_to.default_content()

    def enter_passworld_and_verification(self, passworld='j&cghhbrn39aqS5E'):   #(depth 2)
        passworld_space = self.find_element(By.ID, "password")
        # remplissage du passworld
        self.send_keys_like_hooman(passworld_space, passworld)
        confirmation_space = self.find_element(
            By.CSS_SELECTOR, "#repeat-password")  
        self.send_keys_like_hooman(confirmation_space, passworld)

    def click_on_next_button(self):                                             #(depth 2)
        # méthode artisanale pour trouver le bouton "Suivant"
        class_w100 = self.find_elements(By.CLASS_NAME, 'w100')
        class_text = list(map(lambda x: x.text, class_w100))
        # print(class_text)
        class_w100[class_text.index('Créer un compte')].click()

    def click_free_button(self):   #(depth 2)
        time.sleep(0.5)
        buttons_list = self.find_elements(By.CLASS_NAME, 'button-outline-norm')
        print("buttonlist", buttons_list)
        if buttons_list[0].text != "Continuer avec Free" : 
            return self.click_free_button()
        buttons_list[0].click()
        print("free button clicked", buttons_list[0].text)

    def enter_verification_email(self, email):

        button = self.find_element(By.ID, 'label_1')
        if button.text != "E-mail" : 
            print("ERROR END PROGRAMM AND CHANGE IP")
        button.click()
        
        email_input = self.find_element(By.ID, "email")
        self.send_keys_like_hooman(email_input, email)

        buttons = self.find_elements(By.CLASS_NAME, "button")
        button = list(filter(lambda x: x.text ==
                      "Obtenir un code de vérification", buttons))[0]
        button.click()

    
##################  YOPMAIL  ####################

    def enter_yopmail_page_and_grab_code(self, adress="elias"):
        self.open_and_switch_tab()
        self.land("yopmail")
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

    

    ###########  WARNING A TESTER ################
    def read_verification_code(self):
        time.sleep(0.7)
        print("Reading...")
        #find a different way to find that does not block the code when there is no mail
        code = self.search_code()
        if code is None:
            # add a click reload button
            button_refresh = self.find_element(By.ID, "refresh")
            button_refresh.click()
            return self.read_verification_code()
        
        
        return code
    
    #Cherche le code et ne le renvoie que si c bon 
    def search_code(self) :
        try : 
            self.switch_to.frame(self.find_element(By.NAME, "ifmail"))
            mail = self.find_elements(By.ID, "mail")
            code = mail[0].text.split("\n")[1]
            self.switch_to.default_content() 
            if code.isnumeric() and len(code) == 6:
                return code
            else :
                return None
        
        except : 
            self.switch_to.default_content()
            return None




############## FIN de YOPMAIL ####################

    def close_tab_and_enter_code(self, code):
        self.close()
        self.switch_to.window(self.window_handles[-1])
        form = self.find_element(By.ID, 'verification')
        self.send_keys_like_hooman(form, code)

        buttons = self.find_elements(By.CLASS_NAME, "button")
        button = list(filter(lambda x: x.text == "Vérifier", buttons))[0]
        button.click()

   
    def connect_to(self, account) : 
        name, passworld = account["name"], account["passworld"]
        self.land("Proton_connexion")
        self.enter_name_and_username(name, passworld)



    
    ###############  LOGIN  ####################
    def enter_name_and_username(self, name='Martin', passworld='azertyuiop'):
        username_space = self.find_element(By.ID, 'username')
        self.send_keys_like_hooman(username_space, name)

        passworld_space = self.find_element(By.ID, 'password')
        self.send_keys_like_hooman(passworld_space, passworld)

        login_button = self.find_element(By.CLASS_NAME, 'button-solid-norm')
        login_button.click()

    ##### INUTILISE #####

    def deconnecting_from_previous(self):
        try:
            menue = self.find_element(By.CLASS_NAME, 'flex-align-items-center')
            menue.click()

        except:
            print('ECHEC')



############## CREER UN COMPTE ############
    
        

###############  INUTILISÉ  ####################
    def click_human_verification(self, mail_adress="yann@mailinator.com"):
        buttons = self.find_elements(By.CLASS_NAME, "tabs-list-link")
        button_text_list = list(map(lambda x: x.text, buttons))
        # print(button_text_list)
        buttons[button_text_list.index("Adresse électronique")].click()
        ask_code = self.find_elements(By.CLASS_NAME, 'button-solid-norm')
        ask_code[0].click()

