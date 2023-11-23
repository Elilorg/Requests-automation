import pandas as pd
import json
import requests
import time
import base64
import bs4



class FreeProxyczScaner : 
    using_selenium  = False
    proxylist_url   = "http://free-proxy.cz/fr/proxylist/country/all/all/ping/all"


    def scan(self, *args) :

        security_levels = list(filter(lambda x : x.isdigit(), args))
        protocols = list(filter(lambda x :not x.isdigit(), args))

        if len(security_levels) == 0 : 
            security_levels = ["all"]
        if len(protocols) == 0 : 
            protocols = ["all"]

        arguments = []
        for security_level in security_levels :
            for protocol in protocols : 
                arguments.append((protocol, security_level))
        
        


        proxyes = []
        for protocol, security_level in arguments :  #Parmis les couples d'arguments http/level1, http/level2, https/level1, https/level2
            url = self.get_url(protocol, security_level)
            html_page = self.get_html(url)                      #Premièrepage

            proxyes += self.get_proxieslist(html_page) 
            nb_pages = self.nb_page(html_page)

            for num_page in range(2, nb_pages + 1) :
                url_page = self.get_url(protocol, security_level, page_number = num_page)
                html_page = self.get_html(url_page)
                proxyes += self.get_proxieslist(html_page)

            


        return self.from_list_to_dic(proxyes)


    def get_url(self, protocol = "all", security = "all" ,page_number = 1) :
        protocols = {"https" : "https", "http" : "http", "socket4" : "socks4", "socket5" : "socks5", "all" : "all"}
        security_levels = {"1" : "level3", "2"  : "level2", "3" : "level1", "4" : "level1", "all" : "all"}
        protocol, security = protocols[protocol], security_levels[security]
    
        country, sortby, page =  'all', 'uptime', "1"
        url = f"http://free-proxy.cz/en/proxylist/country/{country}/{protocol}/{sortby}/{security}/{page_number}"  
        return url

    

    def get_html(self, url):
        ## GET html###
        headers = {"Accept":
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Encoding":
                "gzip, deflate",
                "Accept-Language":
                "en-US,en;q=0.5",
                "Connection":
                "keep-alive",
                "DNT": "1",
                "Host":
                "free-proxy.cz",
                "Upgrade-Insecure-Requests":
                "1",
                "User-Agent":
                "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0"}
        r = requests.get(url, headers=headers)
        html_page = r.text

        return html_page

    
    def from_list_to_dic(self, liste)  : 
        json_list = []
        for pl in liste : 
            if (not pl[0] is None ): 

                if (str_ping := str(pl[9]).split(" ")[0]).isdigit(): 
                    ping = int(str_ping)
                else : ping = None
                if (str_speed := str(pl[7]).split(" ")[0]).isdigit(): 
                    speed = int(str_speed)
                else : speed = None
                if (str_uptime := str(pl[8])[:-1].isdigit()) : 
                    uptime = float(str_uptime)
                else : uptime = None

                security_levels = {"Anonymous" : "2", "Transparent" : "0", "High anonymity" : "3", 'nan' : "1"}
                security_level = security_levels[pl[6]]


                json_list.append({"ip" : pl[0],
                                "port" : pl[1], 
                                "country" : pl[3], 
                                "Speed" :  str(pl[7]), 
                                "uptime" : pl[8],
                                "ping"  : int(pl[9].split(" ")[0]),
                                "security" : pl[6], 
                                "last_update" : pl[10],
                                "protocol" : pl[2]})
        return json_list
    

    def get_proxieslist(self, html_text : str) : 
        try : 
            df = pd.read_html(html_text)[1]
        except Exception as e: 
            raise e

        colonne_ip = df[df.columns[0]]
        for index, ip_64 in enumerate(colonne_ip) :
            colonne_ip[index] = self.decode_ip(ip_64)

        df[df.columns[0]] = colonne_ip
        liste = df.values.tolist()
        return liste
    

    def nb_page(self, html : str) : 
        soup = bs4.BeautifulSoup(html, "html.parser")
        divs = soup.find("div", {"class" : "paginator"}).find_all("a")
        divs = [int(i) for i in list(map(lambda x : x.text, divs)) if i.isdigit()]
        if len(divs) == 0 : 
            return 1
        return max(divs)
    
    def decode_ip(self, column : str) : 
        if   len(column.split('"')) > 1 : 
            return str(base64.b64decode(column.split('"')[1]))[2:-1]
        return None
    


