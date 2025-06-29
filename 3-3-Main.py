from bs4 import BeautifulSoup
import csv
with open("/Users/Allan/Document/Code/Python/Open-Classroom.Base-du-langage-Python/3-2-Index.html", "r") as file:
    soup = BeautifulSoup(file.read(), 'html.parser')


# Extraction des titres de l'onglet et de la page
title = soup.title.string
h1 = soup.find('h1').string

# Création d'un dictionnaire pour stocker les produits et leurs caractéristiques
all_products = dict()

# Extraction de chaque éléments de liste
products = soup.find_all("li")


for product in products:
    # Extractin du nom du produit et de son prix
    name_product = product.find("h2").string
    price_product = product.find("p", class_="price").string
    
    # Création d'une liste afin d'extraire la valeur numérique du prix
    price_list = price_product.split(":")
    all_products[name_product] = {"prix": float(price_list[1].replace('€', '').replace(' ', ''))}
    
    # Création d'une liste afin d'extraire le texte de la description de chaque produit
    description_product = product.find_all('p')[-1].string
    description_list = description_product.split(':')
    description_clean = description_list[1][1:]
    all_products[name_product]['description'] = description_clean

# Conversion de chaque prix en dollar
for product in (all_products):
    prix = all_products[product]['prix']*1.2
    all_products[product]['prix_converti'] = prix
    
# Print de chaque produit avec sa description, son prix original et son prix converti en dollar
    print(product)
    print(f"Description:", all_products[product]['description'])
    print(f"Prix en euros:", all_products[product]['prix'],'€')
    print(f"Prix en dollars:", all_products[product]['prix_converti'],'$')
    print()

with open('3-3-data.csv', 'w') as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter = ",")
    writer.writerow(['Nom', 'Description', 'Prix (€)', 'Prix ($)'])
    for nom, infos in all_products.items():
        writer.writerow([nom, infos['description'], infos['prix'], infos['prix_converti']])

