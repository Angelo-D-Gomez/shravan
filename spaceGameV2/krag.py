from enemy import *
from battle import battle
from random import randint


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
            battle(game, p, goon1)
            battle(game, p, goon2)
            # Reward them a knife if won
            print("You have won the fight, and therefore rewarded a knife.")
            p.items.append("Knife")

        elif option == "2":
            print("The goons now begin to chase you. You start running, and come across a pipe on the ground.")
            print("1. Pick up the pipe and attack 2. Continue to run away")

            option = None
            option = game.playerChoice2("Pick up the pipe and attack", "Continue to run away")

            if option == "1":
                print("You decide to pick up the pipe, which increases your attack damage by 3 HP.")
                p.items.append("Pipe")
                p.attack += 3
                print("You then start to attack the goons.")
                battle(game, p, goon1)
                battle(game, p, goon2)

            if option == "2":
                print("You decide to keep running, but eventually get tired and therefore lose 2 HP.")
                # Tell player that they lost HP due to fatigue from running
                p.currHP -= 2
                # If needed, you can tell player their current HP
                print("You are now forced to fight the goons with your fists as you have nowhere else to go.")
                battle(game, p, goon1)
                battle(game, p, goon2)
                # Tell player they got a knife
                print("You have won the fight, and therefore rewarded a knife.")
                p.items.append("Knife")

# If choice 2 is selected set up an rng scenario for the player to dodge the fight with the goons
    elif choice == "2":
        sneak = randint(1, 5)

        if sneak < 2:
            print("You have successfully snuck past the goons and have made it into the city.")

        else:
            print("You have been caught by the goons! You are now forced to fight them with your fists.")
            goon1 = Enemy("goon1", 5, 4)
            goon2 = Enemy("goon2", 5, 4)
            # Set up the fighting
            battle(game, p, goon1)
            battle(game, p, goon2)

# Everything past this point would apply to all winning scenarios
    print("You have successfully passed the goons and are now headed into the town.")
    print("You then spot Krag walking around, and quickly hide behind a structure.")

    # Add some kind of "background" by adding people the player can talk to
    option = None
    print("Beside you, there are town citizens. Would you like to speak with them to gather more \
information?\n 1. Yes 2. No")
    option = game.playerChoice2("Yes", "No")

    if option == "1":
        print("You go up to one young boy...\n")
        print("That freaky monster is taking over this whole town! What are you doing here?")
        option = None
        print("1. Explain that you are a bounty hunter and want to murder Krag \
    2. Say that you are just there to visit family")
        option = game.playerChoice2("Explain that you are a bounty hunter and want to murder Krag",
                                    "Say that you are just there to visit family")

        # If explaining your actual reasoning, the boy will freak out. Otherwise, the conversation will just end
        if option == "1":
            print("The boy puts his hands on his face and screams.")
            print("Why would you want to do something cruel like that?! I mean, he is still pretty freaky.\n")
            print("You explain the benefits of murdering Krag to the boy.\n")
            print("The boy understands, and gives you more information.")
            print("Ok, ok. I get it now. So, all of a sudden, this freaky monster came into town and has started \
    to scare people, including me! Ever since then, people have tried to stay away from it. But now that it is there, a \
    lot of people are stuck in their homes. There are also these weird goon thingys that are patrolling the town, which \
    you seemed to take care of. Oh... got to go! I will try to see you again!")

        elif option == "2":
            print("Oh... well that is fun! Just be careful of that freaky monster over there.\n")

        print("Someone in the town yells everyone to go inside.")
        print("Everybody goes inside, including you. You end up going into an armour shop, where you find a merchant \
        hiding")
        print("The merchant stands back up, and seems to be in shock.\n")
        print("Oh! Um... sorry about that. What would you like to purchase here?\n")
        print("You explain to the merchant your mission.")
        print("Ahh... I see. Well, you have come to the right place, at the right time! \
        I have just 1 set of armour left in stock. It costs 2 coins. Would you like to have it?")
        print("1. Yes 2. No")
        option = None
        option = game.playerChoice2("Yes", "No")
        if option == "1":
            # If no money for armor
            if p.currency < 2:
                print("So you don't have those 2 coins, eh? Well, I want that annoying monster out of here, so I might \
        as well give you the armour for free")
                p.items.append(armour)
                p.maxHP += 10
                p.currHP += 10
            else:
                # If they have money for armour...
                p.currency -= 2
                p.maxHP += 10
                p.currHP += 10
                print("Thanks for coming! Good luck with your battle!")

        elif option == "2":
            print("Well, alright. Hopefully we will meet again!")

        print("You head outside and Krag instantly turns towards you. You step forward and decide to battle him.")
        KRAG = Enemy("Krag", 10, 8)
        battle(game, p, KRAG)
