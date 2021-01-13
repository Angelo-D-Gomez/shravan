from enemy import *
from battle import battle


def krag(game, p):
    print("Now going to planet Bababoeey to slay Krag the Cruel.")
    print("You land your ship in a parking bay in a packed city.\nBadar knows that he has a hit on him\
His goons are patrolling the town. What do you want to do?\n1. Fight the goons 2. Try to sneak past them.")

    choice = game.playerChoice2("Fight the goons", "Try to sneak past them.")
    # Choice 1 sets up a fight with the goons
    if choice == "1":
        # Set goon health/name
        goon1 = Enemy("goon1", 5, 4)
        goon2 = Enemy("goon2", 5, 4)
# Now set up the fighting
        print("You have chosen to fight the goons.")
        print("You go up to the goons and hit them. The goons then instantly turn towards you. You have no weapon \
still tempted to fight with your fists.")
        # Set up the two options, either fight or run
        print("1. Try to fight with fists 2. Run away")
        option = game.playerChoice2("Try to fight with fists", "Run Away")
        if option == "1":
            print("You decide to punch the goons with your fists.")
            battle(p, goon1)
            battle(p, goon2)
            # Reward them a knife if won
            print("You have won the fight, and therefore rewarded a knife.")
            p.items.append("Knife")
    else:
        print("2")