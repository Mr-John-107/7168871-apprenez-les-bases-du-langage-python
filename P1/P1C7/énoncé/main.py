# Créer un dictionnaire "fruit"
fruits = {
    "pomme":"rouge",
    "banane":"jaune",
    "orange":"orange"
}
print(fruits)

# Ajout de la clé "kiwi" avec la valeur "vert"
fruits["kiwi"] = "vert"
print(fruits)

# Accèder à la valeur de "banane" et la stocker dans la variable "couleur_banane"
couleur_banane = fruits.get("banane")

# Modification de la valeur associé à la clé "pomme" pour "vert"
fruits["pomme"] = "vert"

# Suppression de la clé "banane" du dictionnaire
fruits.pop("banane")
print(fruits)

# Affichage du restant des clés
print(fruits.keys())
