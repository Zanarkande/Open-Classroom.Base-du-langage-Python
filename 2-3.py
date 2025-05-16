# Ecrivez votre code ici



def salaire_mensuel(a):
    resultat_mensuel = a / 12
    return resultat_mensuel

def salaire_hebdo(b):
    resultat_hebdo = b / 4
    return resultat_hebdo

def salaire_horaire(c, d):
    resultat_horaire = c / d
    return resultat_horaire


salaire_annuel = (input("Entrez votre salaire annuel: "))
try:
    float(salaire_annuel)
except ValueError:
    raise SystemExit("Erreur: veuillez entrer un nombre.")
salaire_annuel = float(salaire_annuel)


nbr_heure = (input("Entrez votre nombre d'heures travaillées: "))
try:
    float(nbr_heure)
except ValueError:
    raise SystemExit("Erreur: veuillez entrer un nombrre.")
nbr_heure = float(nbr_heure)

mensuel = salaire_mensuel(salaire_annuel)
hebdo = salaire_hebdo(mensuel)
horaire = salaire_horaire(hebdo, nbr_heure)

print(f"Votre salaire horaire cette semaine est de ${horaire}")