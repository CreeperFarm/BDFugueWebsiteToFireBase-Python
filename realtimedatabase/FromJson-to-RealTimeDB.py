# Import database module.
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

# Fetch the service account key JSON file contents
cred = credentials.Certificate('path/to/serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mangathequeapp-default-rtdb.europe-west1.firebasedatabase.app/'
})

# Intitialize the app with the service account
cred = credentials.Certificate("path/to/serviceAccountKey.json")

# Intitialize the value 
file_to_open = 'data_scrap.json'
base_ref = 'all_manga'

print("Starting the script...")

# Get the data from the json file and add it to the database
with open(file_to_open, "r", encoding='utf-8') as json_file:
    dicts = json.load(json_file)
    print("Data loaded from " + file_to_open)
    print("Starting to send data to realtime database...")

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
        tomeNumber: {
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
        }}
        ref = db.reference(base_ref)
        manga_ref = ref.child(i['manga'])
        manga_ref.set(manga_add_list)
        try:
            print(manga_add_list + "is sent to realtime database !")
        except:
            print("Couldn't print data send to realtime database of " + i['manga'] + " book number " + i['tome_number'])

    print("Data sent to realtime database !")

with open(file_to_open, "w", encoding='utf-8') as json_file:
    json.dump([], json_file)

print("Script finished !")


"""collection_name = 'users'
dbinfo = db.reference(collection_name)
dbinfos = dbinfo.get()

print(dbinfos)
dbinfos = list(dbinfos.values())
print(dbinfos)

with open('./data_fire.json', encoding='utf-8') as json_file:
    dicts = json.load(json_file)

for info in dbinfos:
    dicts.append(info.to_dict())    
    print(f"{info.id} => {info.to_dict()}")

with open('./data_fire.json', 'w', encoding='utf-8') as json_file:
    json.dump(dicts, json_file, indent=4, sort_keys=True)
    
with open('./data_fire.json', encoding='utf-8') as json_file:
    data = json.load(json_file)"""


"""# Importation de la librairie firebase_admin
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
collection_name = "Demon slayer"
dbinfo = db.collection(collection_name)
dbinfos = dbinfo.stream()

with open('data.json', encoding='utf-8') as json_file:
    dicts = json.load(json_file)


for manga in dbinfos:
    dicts.append(manga.to_dict())    
    print(f"{manga.id} => {manga.to_dict()}")

with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(dicts, json_file, indent=4, sort_keys=True)
    
with open('data.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
# for i in data:
#    print("Genre : ", i['type'])
"""