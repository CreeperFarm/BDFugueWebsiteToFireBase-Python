
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

with open('data_scrap.json', "r", encoding='utf-8') as json_file:
    dicts = json.load(json_file)
    for i in dicts:
        author = i['author']
        author2 = i['author2']
        available = i['available']
        ean = i['ean']
        editor = i['editor']
        img = i['img']
        manga = i['manga']
        pageNumber = i['pageNumber']
        price = i['price']
        releaseDate = i['releaseDate']
        resume = i['resume']
        tomeNumber = i['tomeNumber']
        type = i['type']
        manga_add_list = {
            "author": str(author),
            "author2": str(author2),
            "available": str(available),
            "ean": str(ean),
            "editor": str(editor),
            "img": str(img),
            "manga": str(manga),
            "pageNumber": str(pageNumber),
            "price": str(price),
            "releaseDate": str(releaseDate),
            "resume": str(resume),
            "tomeNumber": str(tomeNumber),
            "type": str(type)
        }
        mangadb = db.collection(manga)
        mangas = mangadb.stream()
        update_time, mangaadd_ref = db.collection(manga).add(manga_add_list)
        print(f"Added document with id {mangaadd_ref.id}")
        
with open('data_scrap.json', "w", encoding='utf-8') as json_file:
    json.dump([], json_file)