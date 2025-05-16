# Dans le fichier principal, on peut importer les fonctions de `operations.py`
# à l'aide de l'instruction `import` , puis les utiliser pour effectuer des opérations.

import operations

a = input('Entrez votre premier nombre:')
b = input('Entrez votre deuxième nombre:')

try:
    float(a)
except ValueError:
    raise SystemExit("Erreur: veuillez entrer un nombrre.")
a = float(a)

try:
    float(b)
except ValueError:
    raise SystemExit("Erreur: veuillez entrer un nombrre.")
b = float(b)

# Utilisation de la fonction addition
resultat_addition = operations.addition(a, b)
print("Résultat de l'addition :", resultat_addition)
# Utilisation de la fonction multiplication
resultat_multiplication = operations.multiplication(a, b)
print("Résultat de la multiplication :", resultat_multiplication)
