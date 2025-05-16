# Écrivez votre code ici !

import os
from bs4 import BeautifulSoup

# Obtenir le chemin du script
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "3-2-Index.html")

with open(file_path, 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

title = soup.title.string
h1 = soup.find('h1').string

all_products = dict()
products = soup.find_all("li")

#print(products)
for product in products:
    print(product.find("h2").string)