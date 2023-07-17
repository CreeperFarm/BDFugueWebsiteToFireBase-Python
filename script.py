# Importation de la librairie firebase_admin
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialisation de l'application avec les informations du compte de service
cred = credentials.Certificate("path/to/serviceAccountKey.json")


# Application Default credentials are automatically created.
app = firebase_admin.initialize_app(cred)
db = firestore.client()

# Récupération des données de la base de données

mangadb = db.collection("manga")
mangas = mangadb.stream()

for manga in mangas:
    print(f"{manga.id} => {manga.to_dict()}")
    
# Ajout d'un manga dans la base de données
#mangaadd = db.collection("manga").document("drstone111")
#mangaadd.set({'img': 'drs', 'manga': 'Dr. Stone 5555', 'author': 'Riichirô Inagaki', 'type': 'shonen', 'editor': 'Glénat'})
mangaadd = {'img': 'drs', 'manga': 'Dr. Stone 5555', 'author': 'Riichirô Inagaki', 'type': 'shonen', 'editor': 'Glénat'}
update_time, mangaadd_ref = db.collection("cities").add(mangaadd)
print(f"Added document with id {mangaadd_ref.id}")