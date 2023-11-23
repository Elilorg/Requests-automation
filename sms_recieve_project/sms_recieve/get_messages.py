from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

def recup_messages(lien : str) : 

    chrome_options = webdriver.ChromeOptions()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'    
    chrome_options.add_argument('user-agent={0}'.format(user_agent))
    chrome_options.add_argument("--headless")
    
    os.environ['PATH'] += r"C:/Selenium Drivers"
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(lien)
    
    
    
    driver.implicitly_wait(15)
    driver.maximize_window()
    divs_border_bottom = driver.find_elements(By.CLASS_NAME,"border-bottom")
   
    set_of_messages = list(map(lambda x : x.text.split("\n"),divs_border_bottom))
   
    data = []
    for i in set_of_messages :
        data.append(
            {
                "name" : i[0] ,
                "message" : i[2] ,
                "time" : i[1]
            }
        )
    
    return data



