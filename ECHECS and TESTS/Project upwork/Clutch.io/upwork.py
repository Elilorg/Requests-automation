
import requests
headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/237.84.2.178 Safari/537.36'}
for i in range(1000) : 

    r = requests.get(f"https://clutch.co/developers?page={i}", headers=headers)
    print(r.status_code)
