
nom_contact = "Allan"

contact_infos = {"nom": "Blanc", "prenom": "Allan", "telephone": "347-223-7213","email": "allanblanc@gmail.com"}
print(nom_contact)
# print(contact_infos)
# print(contact_infos['email'])

contact_infos["email"] = "strayon9@orange.fr"
# print(contact_infos["email"])

contacts = []
contacts.append(contact_infos)

# print(contacts)

contact2_infos = {"nom": "Jackson", "prenom": "Michael", "telephone": "06 22 02 92 01","email": "Le_J@gmail.com"}
contacts.append(contact2_infos)

# print(contacts)

contacts.remove(contact2_infos)
print(contacts)
print(len(contacts))

input("Entre un truc :")