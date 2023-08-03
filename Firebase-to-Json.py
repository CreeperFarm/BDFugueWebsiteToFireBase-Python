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
