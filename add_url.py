from tkinter import *
from tkinter import ttk
import json

fenetre = Tk()
fenetre.title("Ajout d'url")
base = "https://bdfugue.com/"

fenetre.grid_columnconfigure(0, weight=1)
fenetre.grid_columnconfigure(1, weight=1)
fenetre.grid_columnconfigure(2, weight=1)
fenetre.grid_rowconfigure(0, weight=1)
fenetre.grid_rowconfigure(1, weight=1)
fenetre.grid_rowconfigure(2, weight=1)
fenetre.grid_rowconfigure(3, weight=1)
fenetre.grid_rowconfigure(4, weight=1)
fenetre.grid_rowconfigure(5, weight=1)
fenetre.grid_rowconfigure(6, weight=1)
fenetre.grid_rowconfigure(7, weight=1)
fenetre.grid_rowconfigure(8, weight=1)

label = Label(fenetre, text="Entrée le nom du manga (ex: one-piece)")
label.grid(column=0, row=0)
entrystartlink = Entry(fenetre, textvariable=str, width=35)
entrystartlink.grid(column= 1, row=0)
label = Label(fenetre, text="Entrée le numéro de début de tome a ajouter")
label.grid(column=0, row=1)
entrystartnum = Entry(fenetre, textvariable=int, width=35)
entrystartnum.grid(column=1, row=1)
label = Label(fenetre, text="Entrée le numéro de fin de tome a ajouter")
label.grid(column=0, row=2)
entryendnum = Entry(fenetre, textvariable=int, width=35)
entryendnum.grid(column=1, row=2)
deluxe = ttk.Checkbutton(fenetre, text="Deluxe ?")
deluxe.grid(column=0, row=3)
collector = ttk.Checkbutton(fenetre, text="Collector ?")
collector.grid(column=1, row=3)
edispe = ttk.Checkbutton(fenetre, text="Édition spéciale ?")
edispe.grid(column=2, row=3)
edilimit = ttk.Checkbutton(fenetre, text="Édition limitée ?")
edilimit.grid(column=0, row=4)
edxtra = ttk.Checkbutton(fenetre, text="Edition Xtra (ed xtra) ?")
edxtra.grid(column=1, row=4)
editionxtra = ttk.Checkbutton(fenetre, text="Edition Xtra (edition xtra) ?")
editionxtra.grid(column=2, row=4)
pack = ttk.Checkbutton(fenetre, text="Pack ?")
pack.grid(column=0, row=5)
packaddtome = ttk.Checkbutton(fenetre, text="ajouter la notation tome dans le lien ? (seulement pour pack)")
packaddtome.grid(column=1, row=5)
onetox = ttk.Checkbutton(fenetre, text="X à Y? (seulement pour pack)")
onetox.grid(column=2, row=5)
label = Label(fenetre, text="Entrée le nombre de tome dans le pack (ex: 3)")
label.grid(column=0, row=6)
entrypack = Entry(fenetre, textvariable=str, width=35)
entrypack.grid(column=1, row=6)
label = Label(fenetre, text="Entrée la fin du lien personnalisé (ex: -collection)")
label.grid(column=0, row=7)
entrycustom = Entry(fenetre, textvariable=str, width=35)
entrycustom.grid(column=1, row=7)
bouton = Button(fenetre, text="Envoyer", command=fenetre.quit)
bouton.grid(column=1, row=8)

fenetre.mainloop()
"""
print(entrystartlink.get())
print(entrystartnum.get())
print(entryendnum.get())
print(deluxe.instate(['selected']))
print(collector.instate(['selected']))
print(edispe.instate(['selected']))
print(edilimit.instate(['selected']))
print(entrycustom.get())"""

with open('url.json', "r", encoding='utf-8') as json_file:
    dicts = json.load(json_file)

if pack.instate(['selected']):
    if onetox.instate(['selected']):
        if packaddtome.instate(['selected']):
            start = int(entrystartnum.get())
            end = start + int(entrypack.get()) - 1
            url = str(start) + "-a-" + str(end)
            url = base + "coffret-" + entrystartlink.get() + "-tomes-" + url
            print(url)
            url_new = {
                "url": str(url)
            }
            dicts.append(url_new)
        else:
            start = int(entrystartnum.get())
            end = start + int(entrypack.get()) - 1
            url = str(start) + "-a-" + str(end)
            url = base + "coffret-" + entrystartlink.get() + url
            print(url)
            url_new = {
                "url": str(url)
            }
            dicts.append(url_new)
    else:
        if packaddtome.instate(['selected']):
            start = int(entrystartnum.get())
            end = start + int(entrypack.get()) - 1
            url = ""
            for i in range(start, end):
                url = url + "-" + str(i)
            url = base + "coffret-" + entrystartlink.get() + "-tomes-" + url
            print(url)
            url_new = {
                "url": str(url)
            }
            dicts.append(url_new)
        else:
            start = int(entrystartnum.get())
            end = start + int(entrypack.get()) - 1
            url = ""
            for i in range(start, end):
                url = url + "-" + str(i)
            url = base + "coffret-" + entrystartlink.get() + url
            print(url)
            url_new = {
                "url": str(url)
            }
            dicts.append(url_new)
else:
    for i in range(int(entrystartnum.get()), int(entryendnum.get()) + 1):
        if deluxe.instate(['selected']):
            print(base + entrystartlink.get() + "-tome-" + str(i) + "-deluxe")
            url = base + entrystartlink.get() + "-tome-" + str(i) + "-deluxe"
        elif collector.instate(['selected']):
            print(base + entrystartlink.get() + "-tome-" + str(i) + "-collector")
            url = base + entrystartlink.get() + "-tome-" + str(i) + "-collector"
        elif edispe.instate(['selected']):
            print(base + entrystartlink.get() + "-tome-" + str(i) + "-edition-speciale")
            url = base + entrystartlink.get() + "-tome-" + str(i) + "-edition-speciale"
        elif edilimit.instate(['selected']):
            print(base + entrystartlink.get() + "-tome-" + str(i) + "-edition-limitee")
            url = base + entrystartlink.get() + "-tome-" + str(i) + "-edition-limitee"
        elif edxtra.instate(['selected']):
            print(base + entrystartlink.get() + "-tome-" + str(i) + "-ed-xtra")
            url = base + entrystartlink.get() + "-tome-" + str(i) + "-ed-xtra"
        elif editionxtra.instate(['selected']):
            print(base + entrystartlink.get() + "-tome-" + str(i) + "-edition-xtra")
            url = base + entrystartlink.get() + "-tome-" + str(i) + "-edition-xtra"
        elif entrycustom.get() != "":
            print(base + entrystartlink.get() + "-tome-" + str(i) + entrycustom.get())
            url = base + entrystartlink.get() + "-tome-" + str(i) + entrycustom.get()
        else:
            print(base + entrystartlink.get() + "-tome-" + str(i))
            url = base + entrystartlink.get() + "-tome-" + str(i)
        url_new = {
            "url": str(url)
        }
        dicts.append(url_new)

with open('url.json', "w", encoding='utf-8') as json_file:
    json.dump(dicts, json_file, indent=4, sort_keys=True)
