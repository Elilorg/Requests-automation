import requests
from bs4 import BeautifulSoup
import json
import sms_recieve.const as const
import logging
from sms_recieve.get_messages import recup_messages

# Un find all pour le binaire
def binary_find_all(binary_data: bytes, c: bytes):
    exclamation_index = []
    for index, i in enumerate(binary_data):
        if i == ord('!'):
            exclamation_index.append(index)
    return exclamation_index

# Retirer les commentaire illisibles du code html sous forme binaire
def retirer_commentaires(binary_data: bytes):
    # On regarde l'indice de tout les points d'exclamation
    exclamation_index = binary_find_all(binary_data, b'!')
    # print(exclamation_index)

    # On recupère les intervalles des commentaires html dans un tuple avec indice du premier et dernier caractère
    intervals_commentaires = []
    for i in exclamation_index:
        if binary_data[i-1] == ord('<'):
            # print("ok")
            min = i-1
            max = i-1
            while binary_data[max] != ord('>'):
                max += 1
            intervals_commentaires.append((min, max))

    # On supprime les commentaires html
    for i in intervals_commentaires[1:][::-1]:
        binary_data = binary_data[:i[0]] + binary_data[i[1]+1:]
    return binary_data

# Ici on recupere le page avec requests et on l'inscrit dans un fichier html au numéro correspondant
def recuperer_la_page(numéro_de_page: int):

    # On fait la requete et recuperation du html en binaire avec le numéro de page
    # les headers servent à avoir le bon user-agent
    r = requests.get(
        f'https://www.freereceivesms.com/en/fr/{numéro_de_page}/', headers=const.headers)
    binary_data = r.content

    # Je retire les commentaire du html sous forme binaire
    binary_data = retirer_commentaires(binary_data)

    # on inscrit le code récupéré dans le fichier html nommé avec le numéro de page
    with open(f'./sms_recieve/pages/page{numéro_de_page}.html', 'w') as f:
        f.write(str(binary_data)[2:-1])
    print(f"Page numéro {numéro_de_page} enregistrée")

# On récupère les numéros de toutes les pages de 1 à 10
def recuperer_toutes_les_pages():
    for i in range(1, 11):
        recuperer_la_page(i)


# on ouvre la page (qui se trouve dans le dossier "pages")au numéro donné et on en récupère les numéros et les liens associés.
def recuperer_infos_page(numéro_de_page: int):
    # On récupère le code html du fichier
    with open(f'./sms_recieve/pages/page{numéro_de_page}.html', 'r') as html_file:
        soup = BeautifulSoup(html_file, 'lxml')
        # print(soup.prettify())

    # On récupère les div de chaque numéro
    match = soup.find_all('div', class_='p-3')

    # dans chaque div on recupère le numéro et le lien associé
    numéros = []
    for i in match:
        numéros.append({"numero": i.text[:13], "lien": "https://www.freereceivesms.com" + i.find(
            'a', class_='btn-outline-info').get("href")})
    
    print(f"Page {numéro_de_page} récupérée")
    return numéros

# On récupère les numéros de toutes les pages et on les inscrit dans un fichier json


def recuperer_tout_les_numéros():
    data = []
    for i in range(1, 11):
        data += recuperer_infos_page(i)

    with open(f'./sms_recieve/{const.database_name}', 'w') as f:
        json.dump(data, f)


# cette fonction ne fonctionne pas on va avoir besoin de selenium pour ca
def recupérer_messages_telephone(i: int):
    print(f"Récupérattion des message du telephone numéro {i}")
    # On récupère le numéro à l'index i
    with open(f"./sms_recieve/{const.database_name}", "r") as data:
        dictionnaire = json.load(data)[i]

    # On récupère le lien et le numéro
    numero = dictionnaire["numero"]
    lien = dictionnaire["lien"]
    print(dictionnaire)

    print("sequence selenium démarée, cela peut prendre quelques secondes")
    data = recup_messages(lien)
    return data