
import pandas as pd
import json
import requests
import undetected_chromedriver as uc
import time

class HideMyNameScaner() : 
    using_selenium  =True
    using_requests  : bool
    proxylist_url   = "https://hidemy.name/en/proxy-list/"
    proxylist_name  = "HideMyName"

    def scan(self, *args) -> list[dict]: 
        """
    Scans a webpage and returns a list of dictionaries containing the scraped data.

    Args:
        self: The object instance of the class.

    Returns:
        A list of dictionaries with the scraped data.
    """
        arguments = {"https" : "s", "http" : "h", "socket4" : "4", "socket5" : "5"}

        protocols = "".join([arguments[i] for i in args if not i.isdigit()])
        security_levels = "".join([i for i in args if i.isdigit()])


        url = self.proxylist_url
        if not len(protocols) == 0 :
            url += f"?type={protocols}"
            if not len(security_levels) == 0 :
                url += f"&anon={security_levels}"
        elif not len(security_levels)   == 0 :
            url += f"?anon={security_levels}"

        url += '#list'
        print(url)


        options = uc.ChromeOptions()
        options.headless=True
        options.add_argument('--headless')
        chrome = uc.Chrome(options=options)
        chrome.get(self.proxylist_url)
        time.sleep(5)
        html_page = chrome.page_source
        chrome.quit()

        
     
        #chrome.quit()

        df = pd.read_html('page.html')[0]
        liste = df.values.tolist()     

        #bug les lignes ont des taillles variables
        #liste = [[j.replace("\n", "").replace('"', "") for j in i.split(",")] for i in liste]
        
        print(liste)

        json_variable = []
        for i in liste :
            security_levels = {"High" : "3", "Average" : "2", "Low" : "1", "no" : "1"}
            json_variable +=  [{"ip" : i[0],
                                "port" : i[1], 
                                "country" : i[2], 
                                "Speed" : i[3], 
                                "protocol" : i[4],
                                "security" : security_levels[i[5]], 
                                "last_update" : i[6]}]
        print(json_variable)
        file = open("yes.json", "w")
        json.dump(json_variable, file, indent=4)
        return json_variable