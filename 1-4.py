# Création du dictionnaire 'fruits'
fruits = {
    "pomme": "rouge",
    "banane": "jaune",
    "orange": "orange"
}

# Assigner la couleur du fruit banane à la variable couleur_banane
couleur_banane = fruits["banane"]

# Changer la couleur de la clé 'pomme' par 'vert'
fruits["pomme"] = "vert"

# Retire la clé 'banane' du dictionnaire 'fruits'
fruits.pop("banane")

# Affiche le résultat
print(fruits)
print(couleur_banane)