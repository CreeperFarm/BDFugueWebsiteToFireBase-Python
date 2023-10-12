import json

from selenium import webdriver
from selenium.webdriver.common.by import By

not_ok = []

with open('url_ok.json', 'r', encoding='utf-8') as urls:
    urls_verify = json.load(urls)
    if len(urls_verify) != 0:
        ok = urls_verify
    else:
        print("No url already verify")
        ok = urls_verify

# Créer une inox()stance du navigateur
driver = webdriver.Firefox()


def verify(url):
    driver.get(url)
    try:
        driver.find_element(By.XPATH, "//h1[@class='font-headline cmsp1-text-7xl cmsp1-lg:text-8xl cmsp1-text-gray-900 cmsp1-mb-4 cmsp1-font-bold cmsp1-text-center cmsp1-lg:text-left']")
        print(url + " is not ok")
        url_new = {
            "url": str(url),
        }
        not_ok.append(url_new)
    except Exception:
        print(url + " is ok")
        url_new = {
            "url": str(url),
        }
        ok.append(url_new)


with open('url.json', 'r', encoding='utf-8') as urls:
    url_from_file = json.load(urls)
    if len(url_from_file) != 0:
        for i in url_from_file:
            url = i['url']
            verify(url)

        driver.quit()

        if len(not_ok) == 0:
            print("All those url are ok")
            for i in range(len(ok)):
                with open('url_ok.json', 'w', encoding='utf-8') as urls:
                    json.dump(ok, urls, indent=4, sort_keys=True)
                with open('url.json', 'w', encoding='utf-8') as urls:
                    json.dump(not_ok, urls, indent=4, sort_keys=True)
        else:
            print("All of those url are not ok : ")
            for i in range(len(not_ok)):
                print(not_ok[i])
            for i in range(len(ok)):
                with open('url_ok.json', 'w', encoding='utf-8') as urls:
                    json.dump(ok, urls, indent=4, sort_keys=True)
                with open('url.json', 'w', encoding='utf-8') as urls:
                    json.dump(not_ok, urls, indent=4, sort_keys=True)
    else:
        print("No url to verify")
