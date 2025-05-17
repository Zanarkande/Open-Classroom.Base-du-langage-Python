# Écrivez votre code ici !

# 3.2 Extrayez et transformez des données avec l’extraction web #

from bs4 import BeautifulSoup
with open("/Users/Allan/Document/Code/Python/Open-Classroom.Base-du-langage-Python/3-2-Index.html", "r") as file:
    soup = BeautifulSoup(file.read(), 'html.parser')

title = soup.title.string

h1 = soup.find('h1').string

all_products = dict()

products = soup.find_all("li")

#Extraction et transformation du nom, du prix et de la description de chaque produit puis load dans un dictionnaire
for product in products:
    name_products = product.find("h2").string
    price_products = product.find("p", class_="price").string
    price_list = price_products.split(":")
    all_products[name_products] = {"prix": float(price_list[1].replace('€', '').replace(' ', ''))}
    description_product = product.find_all('p')[-1].string
    description_list = description_product.split(':')
    description_clean = description_list[1][1:]
    all_products[name_products]['description'] = description_clean

# Conversion du prix en dollar
for product in (all_products):
    prix = all_products[product]['prix']*1.2
    all_products[product]['prix'] = prix