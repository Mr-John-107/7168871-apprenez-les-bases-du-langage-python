# Saisir une liste de nombre séparé par une virgule
nombres = input("Entrer une liste de nombre séparé par une virgule: ")

# Transformer la chaîne de caractère par une liste de chaîne de caractère
liste = nombres.split(",")

# Transformer la liste de chaine de caractère en liste d'entier
liste_entier = []
for x in liste:
    x = int(x)
    liste_entier.append(x)

print(liste_entier)

# Somme des nombres de la liste
somme = 0
for x in liste_entier:
    somme += x

print("Somme des nombres: ", somme)

# Moyenne des nombres de la liste
moyenne = somme / len(liste_entier)

print("Moyen des nombres: ", moyenne)

# Nombre de nombre au dessus de la moyenne
nombres_au_dessus_moyenne = 0
for x in liste_entier:
    if x > moyenne:
        nombres_au_dessus_moyenne += 1

print("Nombres au dessus de la moyenne: ", nombres_au_dessus_moyenne)
