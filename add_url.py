from tkinter import *
from tkinter import ttk
import json

fenetre = Tk()
fenetre.geometry("500x500")
fenetre.title("Ajout d'url")
base = "https://bdfugue.com/"

label = Label(fenetre, text="Entrée le nom du manga (ex: one-piece)")
label.pack()
entrystartlink = Entry(fenetre, textvariable=str, width=45)
entrystartlink.pack()
label = Label(fenetre, text="Entrée le numéro de début de tome a ajouter")
label.pack()
entrystartnum = Entry(fenetre, textvariable=int, width=45)
entrystartnum.pack()
label = Label(fenetre, text="Entrée le numéro de fin de tome a ajouter")
label.pack()
entryendnum = Entry(fenetre, textvariable=int, width=45)
entryendnum.pack()
deluxe = ttk.Checkbutton(fenetre, text="Deluxe ?")
deluxe.pack()
collector = ttk.Checkbutton(fenetre, text="Collector ?")
collector.pack()
edispe = ttk.Checkbutton(fenetre, text="Édition spéciale ?")
edispe.pack()
edilimit = ttk.Checkbutton(fenetre, text="Édition limitée ?")
edilimit.pack()
edxtra = ttk.Checkbutton(fenetre, text="Edition Xtra (ed xtra) ?")
edxtra.pack()
editionxtra = ttk.Checkbutton(fenetre, text="Edition Xtra (edition xtra) ?")
editionxtra.pack()
pack = ttk.Checkbutton(fenetre, text="Pack ?")
pack.pack()
packaddtome = ttk.Checkbutton(fenetre, text="ajouter la notation tome dans le lien ? (seulement pour pack)")
packaddtome.pack()
onetox = ttk.Checkbutton(fenetre, text="X à Y? (seulement pour pack)")
onetox.pack()
label = Label(fenetre, text="Entrée le nombre de tome dans le pack (ex: 3)")
label.pack()
entrypack = Entry(fenetre, textvariable=str, width=45)
entrypack.pack()
label = Label(fenetre, text="Entrée la fin du lien personnalisé (ex: -collection)")
label.pack()
entrycustom = Entry(fenetre, textvariable=str, width=45)
entrycustom.pack()
bouton = Button(fenetre, text="Envoyer", command=fenetre.quit)
bouton.pack()

fenetre.mainloop()
print(entrystartlink.get())
print(entrystartnum.get())
print(entryendnum.get())
print(deluxe.instate(['selected']))
print(collector.instate(['selected']))
print(edispe.instate(['selected']))
print(edilimit.instate(['selected']))
print(entrycustom.get())

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
