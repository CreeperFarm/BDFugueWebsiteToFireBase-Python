import json

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

new_data = {
	"manga": str(manga_title),
    "author": str(author_name),
    "price": str(price),
    "available": str(available),
    "releaseDate": str(releaseDate),
    "type": str(type),
    "resume": str(resume),
    "editor": str(editor),
    "pageNumber": str(pageNumber),
    "ean": str(ean),
}
new_data_obj = json.loads(new_data)

with open('data_scrap.json', "w") as data_scrap:
    json.dump(new_data_obj, data_scrap, indent=2)
with open('data_scrap.json', "r") as data_scrap:
    data = json.load(data_scrap)
    
print(data)