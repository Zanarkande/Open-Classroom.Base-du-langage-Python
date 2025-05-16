# définition de la liste [fruits]
fruits = ['pomme', 'banane', 'orange' ]

# ajout de 'kiwi'
fruits.append('kiwi')

# suppresion de 'orange'
fruits.remove ('orange')

# modification de 'banane' par 'ananas'
fruits[1]='ananas'

# affichage de la longueur de la liste
print("La liste fruits contient", len(fruits), "éléments")

# tri de la liste par ordre alphabétique
fruits.sort()

# affichage de la liste
print(fruits)