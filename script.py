"""
# Importation de la librairie firebase_admin
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialisation de l'application avec les informations du compte de service
cred = credentials.Certificate("path/to/serviceAccountKey.json")

# Importation 

# Application Default credentials are automatically created.
app = firebase_admin.initialize_app(cred)
db = firestore.client()

# Récupération des données de la base de données

mangadb = db.collection("manga")
mangas = mangadb.stream()

for manga in mangas:
    print(f"{manga.id} => {manga.to_dict()}")
    
# Ajout d'un manga dans la base de données
"""
"""
mangaadd = {'img': 'drs', 'manga': 'Dr. Stone 5555', 'author': 'Riichirô Inagaki', 'type': 'shonen', 'title': 'Glénat'}
update_time, mangaadd_ref = db.collection("manga").add(mangaadd)
print(f"Added document with id {mangaadd_ref.id}")
"""
"""
from selectorlib import Extractor
import requests 
import json 
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('url', help='Amazon Product Details URL')
# Créer un extractor à partir de la elcture du fichier YAML
e = Extractor.from_yaml_file('Amazon.yml')
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
headers = {'User-Agent': user_agent}
# Télécharger la page en utilisant requests
args = argparser.parse_args()
r = requests.get(args.url, headers=headers)
# Passe le HTML de la page et créer
data = e.extract(r.text)
# Imprimer les données 
print(json.dumps(data, indent=True))
    """

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

available = driver.find_element(By.ID, 'availability') # A fix
print(available.text)