# BDFugue Website To FireBase Real Time DataBase in Python

A Python Program that use BDFugue Website with data grab by Selenium and FireBase Admin API to connect them to automaticly deliver information from BDFugue Website to A Real Time DataBase on FireBase.

[![wakatime](https://wakatime.com/badge/user/c21fbe25-694d-4415-9541-9ff274316f89/project/c7b2069b-7921-4fca-bc51-f16d5a01cc9c.svg)](https://wakatime.com/badge/user/c21fbe25-694d-4415-9541-9ff274316f89/project/c7b2069b-7921-4fca-bc51-f16d5a01cc9c)
![example workflow](https://github.com/CreeperFarm/BDFugueWebsiteToFireBase-Python/actions/workflows/<WORKFLOW_FILE>/badge.svg)

 For this project I use:

[![My Skills](https://skillicons.dev/icons?i=python,selenium,github,vscode)](https://skillicons.dev)

<<<<<<< HEAD
## Table of contents

* [The Requirements](#to-use-this-project-you-need)
* [How to use this project](#how-to-use-this-project)
  * [Step 1 : Create a FireBase Real Time DataBase](#step-1--create-a-firebase-real-time-database)
  * [Step 2 : Get the service account key](#step-2--get-the-service-account-key)
  * [Step 3 : Install Python and the dependencies on your project](#step-3--install-python-and-the-dependencies-on-your-project)
  * [Step 4 : Create file to store your data](#step-4--create-file-to-store-your-data)
  * [Step 5 : Use the project as you want](#step-5--use-the-project-as-you-want)
* [How to](#how-to)
  * [How to change the web driver](#how-to-change-the-web-driver)
  * [How to change the FireBase Real Time DataBase collection name](#how-to-change-the-firebase-real-time-database-collection-name)

## To use this project, you need

* Python 3, personally I use Python 3.11.5 .
* Selenium, you can install it with `pip install selenium`.
* A FireBase Real Time DataBase, you can create one [here](https://firebase.google.com/).
* FireBase Admin, you can install it with `pip install firebase-admin`.
* Json, you can install it with `pip install json`.
* Tkinter, you can install it with `pip install tkinter` for the interface.
* [Optional] ChromeDriver, you can download it [here](https://chromedriver.chromium.org/downloads) (you need to have the same version of Chrome and ChromeDriver) This is needed only if you don't use the last Selenium version.

## How to use this project

### Step 1 : Create a FireBase Real Time DataBase

Go to [FireBase](https://firebase.google.com/) , log-in into your Google Account and create a new project, then go to the project and click on "Real Time DataBase" and create a new one.

### Step 2 : Get the service account key

Go to the parameter of your FireBase Project then, go Account Service and click on "SDK Admin Firebase" then Python and click on "Generate new private key" and save the file in the `PROJECT_FOLDER/path/to/` , with `serviceAcoountKey.json` as name and then your file could be use to send data to your FireBase Real Time DataBase.

### Step 3 : Install Python and the dependencies on your project

Install Python 3, you can download it [here](https://www.python.org/downloads/) on your computer and then go to the project folder and open a terminal and type :

```pip
pip install selenium
pip install firebase-admin
pip install json
pip install tkinter
```

### Step 4 : Create file to store your data

In your Project folder, you need to create url.json, url_ok.json, data.json and data_scrap.json with inside of them this: ```[]```.

### Step 5 : Use the project as you want

To use the project, you can do different things to start,

* You can grab the data you already have inside your real time database with `Firebase-to-Json.py` (if your collection name in your database is not "manga" then see how to change it inside this project on : [How to change the FireBase Real Time DataBase collection name inside this project](#how-to-change-the-firebase-real-time-database-collection-name)).
* You can use `add_url.py` to use a little interface to add url to `url.json`.
* [Warning: you must use `add_url.py` before running this] You can use `url_verifier.py` to lauch the verfier who will lauch the webdriver and check if the url in `url.json` to see if they are usable to get data or not and if they are, it will add them to `url_ok.json` and for the one that don't work they will be the only urls remaining on `url.json` and you should find yourself the url that work for the Manga you want to grab the data to change those url you should go to `url.json` then you must have the code below, than you should change the url who is between the quotes to the one who work  and then you can relaunch `url_verifier.py` to check if the url are usable or not by the bot (`%manga_name%` is the manga name that you have set and `%tome_number%` is the number set).

```json
[
    {
        "url": "https://www.bdfugue.com/%anime_name%-tome-%tome_number%"
    },
    {
        "url": "https://www.bdfugue.com/%anime_name%-tome-%tome_number%"
    },
    ...
]
```

* [Warning: you must use `url_verifier.py` before running this] You can use `FromWeb-to-Json` to lauch the scraper who will lauch the webdriver and get the urldata from the url in `url_ok.json` and then add the data scrap to `data_scrap.json`.

## How to

### How to change the web driver

To change the web driver for :

* `url_verifier.py` go to line 18 and change the `webdriver.Firefox()` to the one you want to use.
* `FromWeb-to-Json.py` go to line 58 and change the `webdriver.Firefox()` to the one you want to use.

### How to change the FireBase Real Time DataBase collection name

To change the collection name of your database inside this project you should change the collection name in those files and replace `manga` by the name of you're collection on firebase :

* `Firebase-to-Json.py` on line 17 ```collection_name = "manga"``` and change the name who is between the quotes
* `Json-to-Firebase.py` on line 14  ```collection_name = "manga"``` and change the name who is between the quotes
=======
## To use this project, you need :
>>>>>>> 739fda5c1b38843cd339dc3bdb5995f3dd7ceff3
