import requests
import bs4
import time
name = "patrik"
from datetime import datetime as t


time_now  = str(t.now())[11 : 16]
with requests.Session() as s:
    r1 = s.get("https://yopmail.com/fr/")
    # print(r1.text)
    soup = bs4.BeautifulSoup(r1.text, "lxml")
    # print(soup.prettify())
    yp = soup.find("input", id="yp").get("value")
    data = {"yp": yp, "login": name}
    time.sleep(2)
    r2 = s.post("https://yopmail.com/fr/", data=data)
    # print(r2.text)
    with open("pagemail.html", "w") as f:
        #print(r2.text[3560: 3580])
        f.write(r2.text[:3571]+r2.text[4577])
    webmailjs = s.get("https://yopmail.com/ver/5.6/webmail.js")
    index = webmailjs.text.find("'inbox?login='")
    yj = webmailjs.text[index:index + 120].split("=")[6]
    params = {
        "login": name,
        "p": "1",
        "d": "",
        "ctrl": "",
        "yp": yp,
        "yj": yj,
        "v": "5.6",
        "r_c": "",
        "id": ""
    }
    print(s.cookies.get_dict())
    cookies_dict = s.cookies.get_dict()
    yses = cookies_dict["yses"]
    ycons = cookies_dict["ycons"]

    headers = {
        
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3', 
        "Cache-Control": "no-cache",
        "Connection": "keep-alive", 
        "Cookie": f"yc={name}; yses={yses}; ycons={ycons}; ytime={time_now}; compte={name}; ywm={name}", 
        "DNT": "1",
        "Host": "yopmail.com",
        "Pragma": "no-cache", 
        "Referer": "https://yopmail.com/fr/wm", 
        "Sec-Fetch-Dest": "iframe", 
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"}

    
    #Essayer de remplir les headers et de les ajouters à la requete pour l'inbox
    #essayer de voir les header d'une requete(et pas une réponse pour voir les headers que met requests par défaut)
    

    inbox = s.get("https://yopmail.com/fr/inbox", params=params)
    with open("inbow.html", "w") as inbox_file:
        inbox_file.write(inbox.text)
        print(inbox)
        print(inbox.url)
        print(inbox.cookies.get_dict())
