import requests
import random
from Packagename.externals_functions import creating_pass_and_user_name, sleep_random
from Packagename.externals_functions import DATABASE

#proxys  = ['34.97.94.207', '103.69.108.78:8191', '40.119.236.22:80', '20.206.106.192:80', '20.24.43.214:80', '20.205.61.143:80']
#['http://ofhiuscm:qvx3fg7x80gn@45.155.68.129:8133', 'http://ofhiuscm:qvx3fg7x80gn@188.74.210.207:6286', 'http://ofhiuscm:qvx3fg7x80gn@185.199.231.45:8382', 'http://ofhiuscm:qvx3fg7x80gn@188.74.183.10:8279', 'http://ofhiuscm:qvx3fg7x80gn@185.199.229.156:7492']

class AccountGenerator : 
    def créer_compte(self,email=None, password=None, date_naissance=None) : 


        _name, passw = creating_pass_and_user_name()
        if email is None : 
            email = f"{_name}@gmail.com"
        else : 
            _name = email.split("@")[0]
        
        if password is None : 
            password = passw
        
        if date_naissance is None : 
            mois = random.randint(1, 12)
            jour = random.randint(1, 28)
            annee = random.randint(1980, 2000)
        else:
            mois, jour, annee = list(map(int, date_naissance.split("/")))

        
        url = "https://spclient.wg.spotify.com:443/signup/public/v1/account/"

        payload = {
            "email" :  email, 
            "password_repeat": password, 
            "password" : password, 
            "key" : "142b583129b2df829de3656f9eb484e6",
            "gender" : "male",
            "platform" : "Android-ARM", 
            "creation_point":"client_mobile", 
            "birth_day": str(jour),
            "birth_month": str(mois),
            "iagree" : "true", 
            "app_version" : "849800892", 
            "birth_year":str(annee), 
            "displayname" : _name
        }

        headers = {"Host": "spclient.wg.spotify.com",
                    "User-Agent": "Spotify/8.4.98 Android/26 (Custom Tablet)",
                    "Connection": "keep-alive",
                    "Content-Type": "application/x-www-form-urlencoded"}
        
#        proxy = None
        r = requests.post(url, data = payload, headers = headers)
        print(r.status_code)
        if (json_res := r.json())["status"] != 1 : 
            raise Exception(json_res["status"], json_res)
        print(r.json()) 
        database = DATABASE()
        database.append({"name" : _name, "email" : f"{_name}@yopmail.com", "password" : password, "id" : database.last_id})
        return _name, password
        
         
        
    def demarrer_requetes(self) : 
        while True : 
            self.créer_compte()
            sleep_random(1, 2)

