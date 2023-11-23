import requests
from datetime import datetime
import bs4
import time

time_now = str(datetime.now())[11 : 16]
s = requests.Session()

name = 'jean'

s.headers.update(
    {
        "Host": "yopmail.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
        "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-User": "?1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
    }
)


################    Page principale  ############
r = s.get(
    "https://yopmail.com/fr/",
    headers={
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Referer": "https://www.google.com/",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
    },
)

soup = bs4.BeautifulSoup(r.text, "lxml")
print(soup.prettify())
yp = soup.find("input", id="yp").get("value")
print(f"yp : {yp}")



# These variables probably come from the result of the request above
Origin_1 = "https://www.google.com"
Referer_1 = "https://yopmail.com/"
Referer_2 = "https://yopmail.com/fr/"
Referer_3 = "https://yopmail.com/ver/5.6/style.css"
Origin_2 = "https://yopmail.com"
Referer_4 = "https://fonts.googleapis.com/"


s.headers.update({"Upgrade-Insecure-Requests": None, "Sec-Fetch-User": None})




s.headers.update({"Sec-Fetch-Mode": "no-cors"})


r = s.get(
    "https://fonts.googleapis.com/css",
    params={"family": "Material Icons Outlined", "display": "block"},
    headers={
        "Host": "fonts.googleapis.com",
        "Accept": "text/css,*/*;q=0.1",
        "Referer": Referer_1,
        "Sec-Fetch-Dest": "style",
        "Sec-Fetch-Site": "cross-site",
    },
)


# These variables probably come from the result of the request above
Referer_5 = "https://fonts.googleapis.com/"


s.headers.update({"Sec-Fetch-Site": "same-origin"})


#recupérer les cookies de la requete 
cookies_dict = s.cookies.get_dict()
#print(f"SESSION COOKIES 1: {cookies_dict}")

yses = cookies_dict["yses"]
print(f"yses : {yses}")
ycons = cookies_dict["ycons"]
print(f"ycons : {ycons}")
yc = cookies_dict["yc"]
print(f"yc : {yc}")


##Recupération du css
r = s.get(
    "https://yopmail.com/ver/5.6/style.css",
    headers={
        "Accept": "text/css,*/*;q=0.1",
        "Referer": Referer_2,
        "Cookie": f"yc={yc}; yses={yses}; ycons={ycons}",
        "Sec-Fetch-Dest": "style",
    },
)

##recupération de webmail.js PAGE 1
r = s.get(
    "https://yopmail.com/ver/5.6/webmail.js",
    headers={
        "Accept": "*/*",
        "Referer": Referer_2,
        "Cookie": f"yc={yc}; yses={yses}; ycons={ycons}",
        "Sec-Fetch-Dest": "script",
    },
)


# These variables probably come from the result of the request above
Origin_3 = "https://yopmail.com"


s.headers.update({"Accept": "image/avif,image/webp,*/*", "Sec-Fetch-Dest": "image"})


##Recupère le logo
r = s.get(
    "https://yopmail.com/pic/YOPmail.png",
    headers={
        "Referer": Referer_3,
        "Cookie": f"yc={yc}; yses={yses}; ycons={ycons}; ytime={time_now}",
    },
)


s.headers.update({"Origin": Origin_3})


#Recupère les polices de caractère 
r = s.get(
    "https://fonts.gstatic.com/s/materialiconsoutlined/v108/gok-H7zzDkdnRel8-DQ6KAXJ69wP1tGnf4ZGhUce.woff2",
    headers={
        "Host": "fonts.gstatic.com",
        "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "identity",
        "Referer": Referer_5,
        "Sec-Fetch-Dest": "font",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
    },
)


s.headers.update({"Origin": None})


####################Recupère les drapaux#############################################
r = s.get(
    "https://yopmail.com/pic/fr.svg",
    headers={
        "Referer": Referer_2,
        "Cookie": f"yc={yc}; yses={yses}; ycons={ycons}; ytime={time_now}",
    },
)
r = s.get(
    "https://yopmail.com/pic/en.svg",
    headers={
        "Referer": Referer_2,
        "Cookie": f"yc={yc}; yses={yses}; ycons={ycons}; ytime={time_now}",
    },
)
r = s.get(
    "https://yopmail.com/pic/es.svg",
    headers={
        "Referer": Referer_2,
        "Cookie": f"yc={yc}; yses={yses}; ycons={ycons}; ytime={time_now}",
    },
)
r = s.get(
    "https://yopmail.com/pic/it.svg",
    headers={
        "Referer": Referer_2,
        "Cookie": f"yc={yc}; yses={yses}; ycons={ycons}; ytime={time_now}",
    },
)
r = s.get(
    "https://yopmail.com/pic/de.svg",
    headers={
        "Referer": Referer_2,
        "Cookie": f"yc={yc}; yses={yses}; ycons={ycons}; ytime={time_now}",
    },
)
r = s.get(
    "https://yopmail.com/pic/pl.svg",
    headers={
        "Referer": Referer_2,
        "Cookie": f"yc={yc}; yses={yses}; ycons={ycons}; ytime={time_now}",
    },
)
r = s.get(
    "https://yopmail.com/pic/ru.svg",
    headers={
        "Referer": Referer_2,
        "Cookie": f"yc={yc}; yses={yses}; ycons={ycons}; ytime={time_now}",
    },
)
r = s.get(
    "https://yopmail.com/pic/uk.svg",
    headers={
        "Referer": Referer_2,
        "Cookie": f"yc={yc}; yses={yses}; ycons={ycons}; ytime={time_now}",
    },
)
r = s.get(
    "https://yopmail.com/pic/zh.svg",
    headers={
        "Referer": Referer_2,
        "Cookie": f"yc={yc}; yses={yses}; ycons={ycons}; ytime={time_now}",
    },
)

########################   FIN DES DRAPAUX ###########################

s.headers.update({"Upgrade-Insecure-Requests": "1"})

r = s.get(
    "https://cdnsure.com/assets/wmv",
    headers={
        "Host": "cdnsure.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Referer": Referer_1,
        "Sec-Fetch-Dest": "iframe",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
    },
)


s.headers.update({"Upgrade-Insecure-Requests": None})


##Recuération d'un gif
r = s.get(
    "https://yopmail.com/favicon.gif",
    headers={
        "Referer": Referer_2,
        "Cookie": f"yc={yc}; yses={yses}; ycons={ycons}; ytime={time_now}",
    },
)


print("sleep...")
time.sleep(1.20986)
#####################    Cookies acceptation         ###################
r = s.get(
    "https://yopmail.com/consent",
    params={"c": "deny"},
    headers={
        "Accept": "*/*",
        "Referer": Referer_2,
        "Cookie": f"yc={yc}; yses={yses}; ycons={ycons}; ytime={time_now}",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
    },
)
print("sleep...")
time.sleep(2.56789)
##########################       Nouvelle page               #################################

#############################################################################################
s.headers.update({"Upgrade-Insecure-Requests": "1", "Origin": Origin_3})

#A cet endroit le cookie ycons change donc je l'update
ycons = s.cookies.get_dict()["ycons"]
print(f'new_ycons : {ycons}')

#Recupération de la page 2 
##changement de ycons
time.sleep(4.56789)
r = s.post(
    "https://yopmail.com/fr/",
    headers={
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Referer": Referer_2,
        "Cookie": f"yc={yc}; yses={yses}; ycons={ycons}; ytime={time_now}",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
    },
    data={"yp": f"{yp}", "login": f"{name}"},  #ATTENTION yp doit etre recup dans le html de la page
)


s.headers.update({"Upgrade-Insecure-Requests": None, "Origin": None, "TE": "trailers"})




s.headers.update({"TE": None})
##Recupération du css
r = s.get(
    "https://yopmail.com/ver/5.6/style.css",
    headers={
        "Accept": "text/css,*/*;q=0.1",
        "Referer": Referer_2,
        "Cookie": f"yc={yc}; yses={yses}; ycons={ycons}; ytime={time_now}; compte={name}; ywm={name}",
        "Sec-Fetch-Dest": "style",
    },
)


##Recupération de webmail.js v2
r = s.get(
    "https://yopmail.com/ver/5.6/webmail.js",
    headers={
        "Accept": "*/*",
        "Referer": Referer_2,
        "Cookie": f"yc={yc}; yses={yses}; ycons={ycons}; ytime={time_now}; compte={name}; ywm={name}",
        "Sec-Fetch-Dest": "script",
    },
)

webmail_js = r.text
index = webmail_js.find("'inbox?login='")
yj = webmail_js[index:index + 120].split("=")[6]


#Recup le capchat
r = s.get(
    "https://www.google.com/recaptcha/api.js",
    params={"onload": "onloadCb", "render": "explicit"},
    headers={
        "Host": "www.google.com",
        "Accept": "*/*",
        "Referer": Referer_1,
        "Sec-Fetch-Dest": "script",
        "Sec-Fetch-Site": "cross-site",
    },
)
print("CAPCHAT")
print(r.content)


####INCLUS le ycons dans les cookies de session
s.headers.update(
    {
        "Cookie": f"yc={yc}; yses={yses}; ycons={ycons}; ytime={time_now}; compte={name}; ywm={name}"
    }
)


##############################  DRAPAUX #####################################
r = s.get(
    "https://yopmail.com/pic/fr.svg",
    headers={"Referer": "https://yopmail.com/fr/wm"},
)
print(r)
r = s.get(
    "https://yopmail.com/pic/en.svg",
    headers={"Referer": "https://yopmail.com/fr/wm"},
)
r = s.get(
    "https://yopmail.com/pic/es.svg",
    headers={"Referer": "https://yopmail.com/fr/wm"},
)
r = s.get(
    "https://yopmail.com/pic/it.svg",
    headers={"Referer": "https://yopmail.com/fr/wm"},
)
r = s.get(
    "https://yopmail.com/pic/de.svg",
    headers={"Referer": "https://yopmail.com/fr/wm"},
)
r = s.get(
    "https://yopmail.com/pic/pl.svg",
    headers={"Referer": "https://yopmail.com/fr/wm"},
)
r = s.get(
    "https://yopmail.com/pic/ru.svg",
    headers={"Referer": "https://yopmail.com/fr/wm"},
)
r = s.get(
    "https://yopmail.com/pic/uk.svg",
    headers={"Referer": "https://yopmail.com/fr/wm"},
)
r = s.get(
    "https://yopmail.com/pic/zh.svg",
    headers={"Referer": "https://yopmail.com/fr/wm"},
)
r = s.get(
    "https://yopmail.com/pic/YOPmail.png",
    headers={"Referer": Referer_3},
)
r = s.get(
    "https://yopmail.com/pic/wait.svg",
    headers={"Referer": Referer_3},
)
####################################  FIN DES DRAPAUX ###########################
s.headers.update({"Origin": Origin_3, "TE": "trailers"})

##Recupération de fonts
r = s.get(
    "https://fonts.gstatic.com/s/materialiconsoutlined/v108/gok-H7zzDkdnRel8-DQ6KAXJ69wP1tGnf4ZGhUce.woff2",
    headers={
        "Host": "fonts.gstatic.com",
        "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "identity",
        "Referer": Referer_5,
        "Sec-Fetch-Dest": "font",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "Cookie": None,
    },
)
print(r)

s.headers.update({"Upgrade-Insecure-Requests": "1", "Origin": None, "TE": None})




##Recupération de inbox
r = s.get(
    "https://yopmail.com/fr/inbox",
    params={
        "login": name,
        "p": "1",
        "d": "",
        "ctrl": "",
        "yp": yp,  ###Doivent etre récupérés###
        "yj": yj,
        "v": "5.6",
        "r_c": "",
        "id": "",
    },
    headers={
        "Cookie" : f'compte={name}; yc={yc}; ycons={ycons}; yses={yses}; ytime={time_now}; ywm={name}',
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Referer": "https://yopmail.com/fr/wm",
        "Sec-Fetch-Dest": "iframe",
        "Sec-Fetch-Mode": "navigate",
    },
    
)

print(r)
#print(r.text)
#print(r.headers)
#print(s.headers)
#print(s.cookies.get_dict())

s.headers.update({"TE": "trailers"})

##IDK
r = s.get(
    "https://cdnsure.com/assets/wmv",
    headers={
        "Host": "cdnsure.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Referer": Referer_1,
        "Sec-Fetch-Dest": "iframe",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Cookie": None,
    },
)


s.headers.update({"Upgrade-Insecure-Requests": None, "Origin": Origin_3, "TE": None})

##CAPCHATS
r = s.get(
    "https://www.gstatic.com/recaptcha/releases/vP4jQKq0YJFzU6e21-BGy3GP/recaptcha__fr.js",
    headers={
        "Host": "www.gstatic.com",
        "Accept": "*/*",
        "Referer": Referer_1,
        "Sec-Fetch-Dest": "script",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "Cookie": None,
    },
)


s.headers.update({"Origin": None})

##Recup une icone
r = s.get(
    "https://yopmail.com/favicon.gif",
    headers={"Referer": Referer_2},
)

##CSS JSP PK
r = s.get(
    "https://yopmail.com/ver/5.6/style.css",
    headers={
        "Accept": "text/css,*/*;q=0.1",
        "Referer": f"https://yopmail.com/fr/inbox?login={name}&p=1&d=&ctrl=&yp={yp}&yj={yj}&v=5.6&r_c=&id=",
        "Sec-Fetch-Dest": "style",
    },
)


r = s.get(
    "https://yopmail.com/pic/wait.svg",
    headers={"Referer": Referer_3},
)

#Recupération d'un mail
r = s.get(
    "https://yopmail.com/fr/mail",
    params={"b": f"{name}", "id": "me_ZwVkZQV0ZGDjAQH2ZQNjZmDkAwDkZt=="}, ###Retrouver cette id , probablement l'id d'un mail
    headers={
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Referer": "https://yopmail.com/fr/wm",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "iframe",
        "Sec-Fetch-Mode": "navigate",
    },
)


s.headers.update(
    {
        "Sec-Fetch-Site": "cross-site",
        "Accept": "text/css,*/*;q=0.1",
        "Sec-Fetch-Dest": "style",
        "TE": "trailers",
    }
)


r = s.get(
    "https://yopmail.com/ver/5.6/style.css",
    headers={
        "Referer": f"https://yopmail.com/fr/mail?b={name}&id=me_ZwVkZQV0ZGDjAQH2ZQNjZmDkAwDkZt==", ###Trouver l'id du mail
        "Sec-Fetch-Site": "same-origin",
        "TE": None,
    },
)


r = s.get(
    "https://fonts.gstatic.com/s/materialiconsoutlined/v108/gok-H7zzDkdnRel8-DQ6KAXJ69wP1tGnf4ZGhUce.woff2",
    headers={
        "Host": "fonts.gstatic.com",
        "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "identity",
        "Origin": Origin_3,
        "Referer": Referer_5,
        "Sec-Fetch-Dest": "font",
        "Sec-Fetch-Mode": "cors",
        "Cookie": None,
    },
)
