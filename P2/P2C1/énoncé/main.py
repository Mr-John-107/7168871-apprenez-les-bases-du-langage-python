# Ecrivez votre code ici !
# Entrer des nombres entier
nombre1 = input("Entrer un nombre entier: ")
nombre2 = input("Entrer un autre nombre entier: ")

# Vérification des nombres dans les chaînes de caractère
if not nombre1.isnumeric() or not nombre2.isnumeric():
    print("Erreur - Ce ne sont des nombres entiers")
    raise SystemExit("Fin du programme")

else: #Conversion en entier
    nombre1 = int(nombre1)
    nombre2 = int(nombre2)

# Choix de l'opération
operation = input("Opération: ")

if operation not in ["+","-","*","/"]:
    print("Erreur - Mauvais signe")
    raise SystemExit("Fin du programme")

else:
    match operation:
        case "+":
            resultat =nombre1 + nombre2
        case "-":
            resultat = nombre1 - nombre2
        case "*":
            resultat = nombre1 * nombre2
        case "/":
            if nombre2 == 0:
                print("Erreur - Un nombre n'est pas divisible par 0")
                raise SystemExit("Fin du programme")
            else:
                resultat = round(nombre1 / nombre2, 2)

# Affichage du résultat
print(f"Le résultat de l'opération est {round(resultat,2)}")
