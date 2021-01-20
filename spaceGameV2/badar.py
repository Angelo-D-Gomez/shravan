from enemy import *
from battle import battle
# May or may not use:
from random import randint


def badar(game, p):
    print("Now going to planet Disco to slay Badar the Barbaric")
    print("You land you ship next to a playground in a very open town.\nBadar's troops find you and are now looking\
directly at you.")
    print("What do you want to do?\n1. Fight the troops 2. Try to run away.")
    choice = game.playerChoice2("Fight the troops", "Try to run away.")

    # If choice is 1, set up fight with troops
    if choice == "1":
        troop1 = Enemy("troop1", 5, 2)
        troop2 = Enemy("troop2", 5, 2)
        troop3 = Enemy("troop3", 5, 2)

        print("You have chosen to fight the troops.")
        battle(game, p, troop1)
        battle(game, p, troop2)
        battle(game, p, troop3)
        p.items.append(" ")
