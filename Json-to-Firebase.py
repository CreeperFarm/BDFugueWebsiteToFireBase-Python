# Import the dependencies needed
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Intitialize the app with the service account
cred = credentials.Certificate("path/to/serviceAccountKey.json")

# Application Default credentials are automatically created.
app = firebase_admin.initialize_app(cred)
db = firestore.client()

# Get the data from the json file and add it to the database
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
        releaseDate = i['release_date']
        resume = i['resume']
        tomeNumber = i['tome_number']
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
        mangadb = db.collection("all_mangas")
        mangas = mangadb.stream()
        mangaadd_ref = db.collection('all_mangas').document(i['manga']).set(manga_add_list)
        # update_time, mangaadd_ref = db.collection(collection_name).document(i['tomeNumber']).set(manga_add_list)
        print(f"Added document with id {mangaadd_ref}")

with open('data_scrap.json', "w", encoding='utf-8') as json_file:
    json.dump([], json_file)
