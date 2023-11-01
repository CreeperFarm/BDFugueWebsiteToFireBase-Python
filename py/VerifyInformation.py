import json
from tkinter import *
from tkinter import ttk
import webbrowser
from PIL import ImageTk
from urllib.request import urlopen

alldata = []

def VerifyPanel(urlhere, a_data_to_verify):
    author = a_data_to_verify['author']
    author2 = a_data_to_verify['author2']
    available = a_data_to_verify['available']
    ean = a_data_to_verify['ean']
    editor = a_data_to_verify['editor']
    img = a_data_to_verify['img']
    manga = a_data_to_verify['manga']
    pageNumber = a_data_to_verify['pageNumber']
    price = a_data_to_verify['price']
    releaseDate = a_data_to_verify['release_date']
    resume = a_data_to_verify['resume']
    tomeNumber = a_data_to_verify['tome_number']
    type = a_data_to_verify['type']
    fenetre = Tk()
    fenetre.title("vérification de " + manga + " tome " + tomeNumber)

    label_author = Label(fenetre, text="Auteur : " + author)
    label_author.grid(column=0, row=0, padx=5, pady=5)
    field_author = Entry(fenetre, width=35)
    field_author.grid(column=1, row=0, padx=5, pady=5)
    label_author2 = Label(fenetre, text="Auteur 2 : " + author2)
    label_author2.grid(column=0, row=1, padx=5, pady=5)
    field_author2 = Entry(fenetre, width=35)
    field_author2.grid(column=1, row=1, padx=5, pady=5)
    label_available = Label(fenetre, text="Disponibilité : " + available)
    label_available.grid(column=0, row=2, padx=5, pady=5)
    field_available = Entry(fenetre, width=35)
    field_available.grid(column=1, row=2, padx=5, pady=5)
    label_ean = Label(fenetre, text="EAN : " + ean)
    label_ean.grid(column=0, row=3, padx=5, pady=5)
    field_ean = Entry(fenetre, width=35)
    field_ean.grid(column=1, row=3, padx=5, pady=5)
    label_editor = Label(fenetre, text="Éditeur : " + editor)
    label_editor.grid(column=0, row=4, padx=5, pady=5)
    field_editor = Entry(fenetre, width=35)
    field_editor.grid(column=1, row=4, padx=5, pady=5)    

    # Image network load
    # TODO: Fix this
    """data = urlopen(img)
    dataimg = data.read()
    data.close()
    image = ImageTk.PhotoImage(dataimg)
    label_img = fenetre.Label(fenetre, image=image)
    label_img.image = image
    label_img.grid(column=0, row=5, padx=5, pady=5)
    field_img_link = Entry(fenetre, width=35)
    field_img_link.grid(column=1, row=5, padx=5, pady=5)"""

    label_manga = Label(fenetre, text="Manga : " + manga)
    label_manga.grid(column=0, row=6, padx=5, pady=5)
    field_manga = Entry(fenetre, width=35)
    field_manga.grid(column=1, row=6, padx=5, pady=5)
    label_pageNumber = Label(fenetre, text="Nombre de pages : " + pageNumber)
    label_pageNumber.grid(column=0, row=7, padx=5, pady=5)
    field_pageNumber = Entry(fenetre, width=35)
    field_pageNumber.grid(column=1, row=7, padx=5, pady=5)
    label_price = Label(fenetre, text="Prix : " + price)
    label_price.grid(column=0, row=8, padx=5, pady=5)
    field_price = Entry(fenetre, width=35)
    field_price.grid(column=1, row=8, padx=5, pady=5)
    label_releaseDate = Label(fenetre, text="Date de sortie : " + releaseDate)
    label_releaseDate.grid(column=0, row=9, padx=5, pady=5)
    field_releaseDate = Entry(fenetre, width=35)
    field_releaseDate.grid(column=1, row=9, padx=5, pady=5)
    label_resume = Label(fenetre, text="Résumé : " + resume, wraplength=300)
    label_resume.grid(column=0, row=10, padx=5, pady=5)
    field_resume = Entry(fenetre, width=35)
    field_resume.grid(column=1, row=10, padx=5, pady=5)
    label_tomeNumber = Label(fenetre, text="Numéro du tome : " + tomeNumber)
    label_tomeNumber.grid(column=0, row=11, padx=5, pady=5)
    field_tomeNumber = Entry(fenetre, width=35)
    field_tomeNumber.grid(column=1, row=11, padx=5, pady=5)
    label_type = Label(fenetre, text="Type : " + type)
    label_type.grid(column=0, row=12, padx=5, pady=5)
    field_type = Entry(fenetre, width=35)
    field_type.grid(column=1, row=12, padx=5, pady=5)
    open_url = Button(fenetre, text="Ouvrir le lien", command=lambda: webbrowser.open(urlhere))
    open_url.grid(column=0, row=13, padx=5, pady=5, sticky="nsew")
    bouton = Button(fenetre, text="Envoyer", command=fenetre.quit)
    bouton.grid(column=1, row=13, padx=5, pady=5, sticky="nsew")
    
    fenetre.mainloop()

    if field_author.get() != "":
        author = field_author.get()
    if field_author2.get() != "":
        author2 = field_author2.get()
    if field_available.get() != "":
        available = field_available.get()
    if field_ean.get() != "":
        ean = field_ean.get()
    if field_editor.get() != "":
        editor = field_editor.get()
    if field_manga.get() != "":
        manga = field_manga.get()
    if field_pageNumber.get() != "":
        pageNumber = field_pageNumber.get()
    if field_price.get() != "":
        price = field_price.get()
    if field_releaseDate.get() != "":
        releaseDate = field_releaseDate.get()
    if field_resume.get() != "":
        resume = field_resume.get()
    if field_tomeNumber.get() != "":
        tomeNumber = field_tomeNumber.get()
    if field_type.get() != "":
        type = field_type.get()
    print("VerifyPanel")
    data_verify = {
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
    alldata.append(data_verify)
    with open('py/data_ok.json', "w", encoding='utf-8') as json_file:
        data = json.dump(alldata, json_file, indent=4, sort_keys=True)

url = []
data_to_verify = []

with open('py/url_ok.json', 'r', encoding='utf-8') as urls:
    url_from_file = json.load(urls)
    for i in url_from_file:
        iurl = i['url']
        url.append(iurl)
    with open('py/data_scrap.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for j in data:
            data_to_verify.append(j)
        k=0
        for j in data_to_verify:
            VerifyPanel(url[k], data_to_verify[k])
            k+=1