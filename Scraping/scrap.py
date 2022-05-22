import pandas
import requests
from bs4 import BeautifulSoup as BS
# Scrapp tofotocasa. Houses in León.
url = "https://www.fotocasa.es/es/comprar/viviendas/leon-capital/todas-las-zonas/l"
df = pandas.DataFrame(columns=["Title", "Price", "Rooms", "Toilets", "Size"])
r = requests.get(url)
index = 2
#To check all the pages with info
while r.status_code != 404:
    c = r.content
    soup = BS(c, "html.parser") 
    
    all = soup.find_all("article",{"class":"re-CardPackPremium"})
    # In fact only the first page is getting houses info :(
    if len(all) == 0:
        break
    # This page only loads the info of the house that are been shown in the web browser, the rest of them has a placeholder but without info
    all2=soup.find_all("div",{"class":"re-CardPackPremiumPlaceholder"})

    for house in all:
        name = house.find("span",{"class":"re-CardTitle re-CardTitle--big"}).text
        price = house.find("span",{"class":"re-CardPrice"}).text
        rooms = house.find("span",{"class":"re-CardFeaturesWithIcons-feature-icon re-CardFeaturesWithIcons-feature-icon--rooms"}).text
        toilets = house.find("span",{"class":"re-CardFeaturesWithIcons-feature-icon re-CardFeaturesWithIcons-feature-icon--bathrooms"}).text
        size = house.find("span",{"class":"re-CardFeaturesWithIcons-feature-icon re-CardFeaturesWithIcons-feature-icon--surface"}).text
        df = df.append({"Title":name, "Price":price, "Rooms":rooms, "Toilets":toilets, "Size":size}, ignore_index=True)
    
    r = requests.get(url + "/" + str(index))
    index+=1

df.to_csv("Scraping\\Houses.csv")
