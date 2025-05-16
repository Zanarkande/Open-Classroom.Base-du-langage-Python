nbr_gauche = input("Entrez un nombre entier : ") # Première valeur
nbr_droite = input("Entrez un nombre entier : ") # Deuxième valeur
symbole = input("Choisissez l'opération souhaitée ['+', '-', '*' ou '/'] :") # Choix de l'opération

resultat = 0

# Vérification si nombres entiers
if not nbr_gauche.isnumeric() or not nbr_droite.isnumeric():
    print("Erreur: les nombres doivent êtres des nombres entiers")
else:
    nbr_gauche = int(nbr_gauche) 
    nbr_droite = int(nbr_droite)


# Vérification du symbole
match symbole:
    case "*":
        print("bon symbole")
    case "/":
        print("bon symbole")
    case "+":
        print("bon symbole")
    case "-":
        print("bon symbole")
    case _:
        print("le symbole n'est pas reconnu")

# Vérification d'une divison par zéro et résultat si pas de problèmes
if symbole == "/" and nbr_gauche == 0 or nbr_droite == 0:
    print("Impossible de réaliser une division par 0")
else:
    match symbole:
        case "*":
            resultat = nbr_gauche * nbr_droite
        case "/":
            resultat = nbr_gauche / nbr_droite
        case "+":
            resultat = nbr_gauche + nbr_droite
        case "-":
            resultat = nbr_gauche - nbr_droite

print(resultat)