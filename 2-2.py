def main():
# Entrée de la list
    liste = input("Entrez une liste de nombres séparés par des virugles: ")

# Séparation de la string en liste
    liste = liste.split(",")
    print("Liste de nombres:", liste)

# Calcul de la somme des éléments de la liste
    somme = 0
    for nombre in liste:
        somme += int(nombre)
    print("Somme des nombres: ", somme)

# Calcul de la moyenne de la liste
    moyenne = somme/len(liste)
    print ("Moyenne:", moyenne)

# Calcul du nombre d'éléments supérieurs à la moyenne de la liste
    nombre_sup_moy = 0
    for nombre in liste:
        if int(nombre) > moyenne:
            nombre_sup_moy += 1
    print("Nombres d'éléments supérieurs à la moyenne: ", nombre_sup_moy)

    nombre_pairs = 0
    i = 0 
    while i < len(liste):
        if int(liste[i]) % 2 == 0:
            nombre_pairs += 1
        i += 1
    print("Combien de nombres pairs ?", nombre_pairs)            
        
if __name__ == "__main__":
    main()