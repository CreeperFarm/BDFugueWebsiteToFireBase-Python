
# Importation de la librairie firebase_admin
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Initialisation de l'application avec les informations du compte de service
cred = credentials.Certificate("path/to/serviceAccountKey.json")

# Importation 

# Application Default credentials are automatically created.
app = firebase_admin.initialize_app(cred)
db = firestore.client()

# Récupération des données de la base de données

mangadb = db.collection("manga")
mangas = mangadb.stream()

with open('data.json', encoding='utf-8') as json_file:
    dicts = json.load(json_file)


for manga in mangas:
    dicts.append(manga.to_dict())    
    print(f"{manga.id} => {manga.to_dict()}")

with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(dicts, json_file, indent=4, sort_keys=True)
    
with open('data.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
#for i in data:
#    print("Genre : ", i['type'])
    
    
# Ajout d'un manga dans la base de données

"""
mangaadd = {'img': 'drs', 'manga': 'Dr. Stone 5555', 'author': 'Riichirô Inagaki', 'type': 'shonen', 'title': 'Glénat'}
update_time, mangaadd_ref = db.collection("manga").add(mangaadd)
print(f"Added document with id {mangaadd_ref.id}")
"""

""" Avec Amazon
# Importation des librairies selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Créer une instance du navigateur
driver = webdriver.Firefox()
driver.get("https://www.amazon.fr/Demon-Slayer-T01-Koyoharu-Gotouge/dp/2809482314/")

# Accepter les cookies
accept_cookie = driver.find_element(By.ID, "sp-cc-accept")
accept_cookie.click()

# Récupérer le titre + le numéro du tome du manga
manga_title = driver.find_element(By.ID, "productTitle")
print(manga_title.text)

# Récupérer l'auteur du manga
manga_author = driver.find_element(By.CLASS_NAME, "author")
print(manga_author.text)

# Récupérer le prix du manga
manga_price = driver.find_element(By.CLASS_NAME, "a-price")
print(manga_price.text)

# Récupérer l'éditeur du manga
info_manga = driver.find_element(By.ID, "detailBullets_feature_div")
print(info_manga.text)

# Récupérer le lien de l'image du manga
#img_link = driver.find_element(By.ID, "landingImage") # A fix
#print(img_link.get_attribute("src"))

# Récuperer le titre du manga
title = driver.find_element(By.CLASS_NAME, "rpi-attribute-value")
print(title.text)

# Récuperer l'éditeur du manga
editor = driver.find_element(By.CLASS_NAME, "rpi-carousel-attribute-card") # A fix
print(editor.text)

# Récuperer la disponibilité du manga
available = driver.find_element(By.ID, 'availability') # A fix
print(available.text)
    """
    
# Importation des url
"""import json

with open('url.json') as url_json:
    url_data = json.load(url_json)
print(url_data)
    
# Importation des librairies selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Créer une instance du navigateur
driver = webdriver.Firefox()
driver.get("https://www.bdfugue.com/demon-slayer-tome-1")

# Récupérer le titre + le numéro du tome du manga
manga_title = driver.find_element(By.CLASS_NAME, "titre-bd-grand")
tomeNumber = manga_title.text.replace("Demon slayer tome ", "")
manga_title = manga_title.text.split(" ")
manga_title = manga_title[0] + " " + manga_title[1]
print(manga_title)
print(tomeNumber)

# Récupérer l'auteur du manga
author_name = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div/div/div[2]/p[1]/a")
author_name = author_name.text
print(author_name)
try :
    author_name2 = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div/div/div[2]/p[2]/a")
    print(author_name2.text)
except Exception as ex:
    author_name2 = ""
    print("Pas d'auteur 2")
    



# Récupérer le prix du manga
price = driver.find_element(By.CLASS_NAME, "price")
price = price.text
print(price)

# Récupérer la disponibilité du manga
available = driver.find_element(By.CLASS_NAME, "availability")
available = available.text.split(" ")
available = available[0] + " " + available[1] + " "

print(available)

# Récupérer la date de sortie du manga
releaseDate = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div/div/p")
releaseDate = releaseDate.text.replace("Date de parution : ", "")
releaseDate = releaseDate.split(" ")

date_dico = {
    "Janvier": "01",
    "Février": "02",
    "Mars": "03",
    "Avril": "04",
    "Mai": "05",
    "Juin": "06",
    "Juillet": "07",
    "Août": "08",
    "Septembre": "09",
    "Octobre": "10",
    "Novembre": "11",
    "Décembre": "12"
}
releaseDate[1] = date_dico[releaseDate[1]]

releaseDate = releaseDate[1] + "/" + releaseDate[0] + "/" + releaseDate[2]
print(releaseDate)

# Récupérer le genre du manga
type = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div/div/div[3]")
type = type.text.replace("Genre : ", "")
type = type.split(" ")

type_dico = {
    "Shonen": "Shōnen",
    "Seinen": "Seinen",
    "Shojo": "Shōjo",
    "Josei": "Josei",
}

if type[0] in type_dico:
    type = type_dico[type[0]]
else:
    type = type[0]

    
print(type)
# Récupérer le résumé du manga
    # Switch frame by id
driver.switch_to.frame('iframe-desc')
resume = driver.find_element(By.ID, "p-iframe")
resume = resume.text.replace("Résumé : ", "")
print(resume)
driver.switch_to.default_content()

# Récupérer l'éditeur du manga
editor = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[2]/div[9]/ul[3]/li[1]/a")
print(editor.text)

# Récupérer le nombre de pages du manga
pageNumber = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[2]/div[9]/ul[2]/li[3]")
pageNumber = pageNumber.text.replace("Nombre de pages : ", "")
print(pageNumber)

# Récupérer l'ean du manga
ean = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[2]/div[9]/ul[2]/li[1]")
ean = ean.text.replace("Référence : ", "")
print(ean)


driver.quit()
"""