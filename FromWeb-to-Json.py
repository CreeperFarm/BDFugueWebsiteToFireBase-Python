""" Ave Amazon
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

# Avec BDFugue
import json

from selenium import webdriver
from selenium.webdriver.common.by import By


# noinspection PyBroadException
def get_manga_info(url):
    # Créer une instance du navigateur
    driver = webdriver.Firefox()
    driver.get(url)

    more_info = driver.find_element(By.XPATH, "//button[@class='btn mt-6 lg:max-w-[284px] lg:ml-[calc(100%/3)]']")
    more_info.click()

    # Récupérer le titre du manga
    manga_title = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/section[1]/div[1]/section/div[2]/div/div[10]/div[2]")
    manga_title = manga_title.text
    print(manga_title)

    # Récupérer le numéro du tome du manga
    tome_number_unsplit = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/section[1]/div[1]/section/div[2]/div/div[11]/div[2]")
    tome_number_unsplit = tome_number_unsplit.text
    tome_number = tome_number_unsplit.split(" ")
    if (tome_number_unsplit == tome_number[0]):
        tome_number = tome_number_unsplit
    else:
        tome_number = tome_number_unsplit
    print(tome_number)

    # Récupérer le type d'édition du manga
    type_edition = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/section[1]/div[1]/div[1]/div/h1")
    type_edition = type_edition.text.replace(manga_title + " ", "")
    type_edition = type_edition.replace(" tome " + tome_number, "")

    try:
        type_edition = type_edition.replace("(", "")
        type_edition = type_edition.replace(")", "")
        try:
            typeedi_dico = {
                "éd. collector": "Édition Collector",
                "édition collector": "Édition Collector",
                "collector": "Édition Collector",
                "deluxe": "Édition Deluxe",
                "édition limitée": "Édition Limitée",
                "éd. limitée": "Édition Limitée",
            }

            if type_edition in typeedi_dico:
                type_edition = typeedi_dico[type_edition]
            else:
                type_edition = type_edition

            print(type_edition)
        except Exception:
            try:
                type_edition = type_edition.replace(" - ", "")
            except Exception:
                print(type_edition)

            print(type_edition)
    except Exception:
        try:
            type_edition = type_edition.replace(" - ", "")
        except Exception:
            if type_edition.text == manga_title + " tome " + tome_number:
                type_edition = "Édition standard"
            else:
                typeedi_dico = {
                    "éd. collector": "Édition Collector",
                    "édition collector": "Édition Collector",
                    "collector": "Édition Collector",
                    "deluxe": "Édition Deluxe",
                    "édition limitée": "Édition Limitée",
                    "éd. limitée": "Édition Limitée",
                }

                if type_edition in typeedi_dico:
                    type_edition = typeedi_dico[type_edition]
                else:
                    type_edition = type_edition

                print(type_edition)

                print("Pas d'édition")

    # Récupérer l'auteur du manga
    author_name = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/main[1]/div[2]/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/div[2]/p[1]/a[1]")
    author_name = author_name.text.replace("\u014d", '0254')
    print(author_name)
    author_name = author_name.replace("0254", "ō")
    try:
        author_name2 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/main[1]/div[2]/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/div[2]/p[1]/a[2]")
        print(author_name2.text)
    except Exception:
        author_name2 = ""
        print("Pas d'auteur 2")

    # Récupérer le prix du manga
    price = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/section[1]/div[2]/div/div[1]/div[1]/div[2]/div/span[2]/span")
    price = price.text
    print(price)

    # Récupérer la disponibilité du manga
    available = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/section[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/span[1]")
    available = available.text.split(" ")
    if available[0] == "Pré-commande":
        available = available[0]
    else:
        available = available[0] + " " + available[1]
    print(available)

    # Récupérer la date de sortie du manga
    release_date = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/section[1]/div[1]/section/div[2]/div/div[12]/div[2]")
    release_date = release_date.text  # .replace("Date de parution : ", "")
    release_date = release_date.split(" ")

    # Remplacer le mois par son numéro associé
    date_dico = {
        "janvier": "01",
        "février": "02",
        "mars": "03",
        "avril": "04",
        "mai": "05",
        "juin": "06",
        "juillet": "07",
        "août": "08",
        "septembre": "09",
        "octobre": "10",
        "novembre": "11",
        "décembre": "12",
        "janv.": "01",
        "févr.": "02",
        "avri.": "04",
        "juil.": "07",
        "sept.": "09",
        "octo.": "10",
        "nove.": "11",
        "déce.": "12"
    }
    release_date[1] = date_dico[release_date[1]]
    # Remise en forme de la date
    release_date = release_date[1] + "/" + release_date[0] + "/" + release_date[2]
    print(release_date)

    # Récupérer le genre du manga
    try:
        type_manga = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/section[1]/div[1]/section/div[2]/div/div[3]/div[2]/a")
        type_manga = type_manga.text  # .replace("Genre : ", "")
        print(type_manga)
        type_manga = type_manga.split(" ")
        # Remplacer le genre par son nom japonais si dans le dico
        type_dico = {
            "Shonen": "Shōnen",
            "Seinen": "Seinen",
            "Shojo": "Shōjo",
            "Josei": "Josei",
        }

        if type_manga[0] in type_dico:
            print(type_manga[0])
            type_manga = type_dico[type_manga[0]]
        else:
            type_manga = type_manga[0]
    except Exception:
        type_manga = "Genre inconnu"
        return "Genre inconnu"

    # Récupérer le résumé du manga
    resume = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/section[1]/div[1]/div[1]/div/div[5]/div/div/div[1]/div")
    resume = resume.text
    try:
        print(resume)
    except Exception:
        print("Impossible de print le résumé à cause d'un caractère spécial")
    """
    try:
        driver.switch_to.frame('iframe-desc')
        resume = driver.find_element(By.ID, "p-iframe")
        resume = resume.text.replace("Résumé : ", "")
        print(resume)
        driver.switch_to.default_content()
    except Exception as ex:
        resume = "Pas de résumé"
        print(resume)
    """

    # Récupérer l'éditeur du manga
    editor = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/section[1]/div[1]/section/div[2]/div/div[4]/div[2]/a")
    editor = editor.text
    print(editor)

    # Récupérer le nombre de pages du manga
    page_number = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/section[1]/div[1]/section/div[2]/div/div[8]/div[2]")
    page_number = page_number.text  # .replace("Nombre de pages : ", "")
    print(page_number)

    # Récupérer l'ean du manga
    ean = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/section[1]/div[1]/section/div[2]/div/div[1]/div[2]")
    ean = ean.text  # .replace("Référence : ", "")
    print(ean)

    # Récupérer le lien de l'image du manga
    img = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/section[1]/div[1]/div[1]/div/div[1]/div/div[2]/div[1]/picture[1]/source[2]")
    img = img.get_attribute("srcset")
    print(img)

    # Quitter le navigateur
    driver.quit()

    # Récupérer les données dans le fichier json
    with open('data_scrap.json', encoding='utf-8') as json_file:
        dicts = json.load(json_file)

    # Création de la liste du nouveau manga
    new_data = {
        'manga': str(manga_title),
        'author': str(author_name),
        'author2': str(author_name2),
        'price': str(price),
        'available': str(available),
        'release_date': str(release_date),
        'type': str(type_manga),
        'resume': str(resume),
        'editor': str(editor),
        'pageNumber': str(page_number),
        'tome_number': str(tome_number),
        'ean': str(ean),
        'img': str(img),
    }
    # Ajouter la liste du nouveau manga dans le fichier json
    dicts.append(new_data)
    with open('data_scrap.json', "w") as data_scrap:
        json.dump(dicts, data_scrap, indent=4, sort_keys=True)

    # Lecture de toute les données du fichier json
    with open('data_scrap.json', "r") as data_scrap:
        data = json.load(data_scrap)

# Commande de debug
# get_manga_info("https://www.bdfugue.com/demon-slayer-tome-1")

# Récupérer les urls des mangas
with open('url_ok.json', 'r', encoding='utf-8') as urls:
    url_from_file = json.load(urls)
    for i in url_from_file:
        url = i['url']
        get_manga_info(url)
with open('url_ok.json', 'w', encoding='utf-8') as urls:
    json.dump([], urls)
