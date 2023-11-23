import requests 
import bs4


def get_free_proxies_list():

    r = requests.get("https://free-proxy-list.net/")

    soup = bs4.BeautifulSoup(r.text, "lxml")
    table1 = soup.table

    with open("page1.html", "w") as table_file: 
        table_file.write(str(table1))

    table = []
    for i in table1.find_all("tr"):
        table.append(
            list(map(lambda x: str(x).split(">")[1][:-4], i.find_all("td"))))

    return table
