# -*- coding: utf-8 -*-

from random import randint

print("\t\t\t\t=== LE JEU DU PLUS OU MOINS ===\n\n")
print("\t\t\t\t=== Choissisez le mode de jeu (Easy-Normal-Hard-CRAZY) ===\n\n")

def choiceMode(num1, num2):

    nombrePropose = 0
    count = 0

    nombreMystere = randint(num1,num2)

    while nombrePropose != nombreMystere:

        print("Choisit un nombre entre " + str(num1) + " et " + str(num2))

        try:
            nombrePropose = int(input())

        except ValueError:

            print("Ce n'est pas un nombre !")

            continue

        else:

            if nombrePropose < nombreMystere:
                print("C'est trop petit !\n")

            elif nombrePropose > nombreMystere:
                print("C'est trop grand !\n")

        count += 1

    print("Félicitations, vous avez trouvé le nombre mystère !!!\n En " + str(count) + " essai(s)")


modeGame = input()
modeGameComplet = modeGame.lower()

if modeGameComplet == "easy":
    choiceMode(1, 50)
elif modeGameComplet == "normal":
    choiceMode(1, 100)
elif modeGameComplet == "hard":
    choiceMode(1, 1000)
elif modeGameComplet == "crazy":
    choiceMode(1, 10000)
else:
    print("Mauvais Choix !")
