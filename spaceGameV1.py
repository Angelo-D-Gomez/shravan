from random import randint


# to use randint(x, y) put a minimum value and a max value to randomly generate in the function
# in no min value is input the default will be zero
class Player:

    def __init__(self, name):
        self.name = name
        self.items = []
        # Note: This is the STARTING maximum HP
        self.maxHP = 10
        self.currHP = 10
        self.attack = 4
        self.currency = 5

    # Make a function inside player to control health changes


# make an enemy class
# enemy class needs to have HP, an attack value, we can use RNG to determine dodge chances
class Enemy:

    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.maxHP = health
        self.attack = attack


class Game:

    def __init__(self, player):
        self.p = player

    def playerChoice2(self, choice1, choice2):
        choice = input()
        while (choice not in ["1", "2"]):
            choice = input("Please enter the number of your choice.\n\
1. " + choice1 + " 2. " + choice2)
        return choice

    # Full battle function; Used for all battle scenarios
    def battle(self, enemy):
        while (self.p.currHP > 0 and enemy.health > 0):
            firstStrike = randint(0, 1)
            if (firstStrike == 0):
                print("The " + enemy.name + " attacks first.")
                eDamage = randint(0, enemy.attack)
                if (eDamage == 0):
                    print("The " + enemy.name + "'s attack missed.")
                else:
                    print("The " + enemy.name + "'s attack did " + str(eDamage) + " damage!")
                    self.p.currHP -= eDamage
                    if self.p.currHP <= 0:
                        print(self.p.name + " has 0 health remaining.")
                    else:
                        print(self.p.name + " has " + str(self.p.currHP) + " health remaining.")
                pDamage = randint(0, self.p.attack)
                if (pDamage == 0):
                    print(self.p.name + "'s attack missed.")
                else:
                    enemy.health -= pDamage
                    print(self.p.name + " attacks and does " + str(pDamage) + " damage.")

            else:
                print(self.p.name + " attacks first!")
                pDamage = randint(0, self.p.attack)
                if (pDamage == 0):
                    print(self.p.name + "'s attack missed.")
                else:
                    enemy.health -= pDamage
                    print(self.p.name + " attacks and does " + str(pDamage) + " damage.")
                eDamage = randint(0, enemy.attack)
                if (eDamage == 0):
                    print("The " + enemy.name + "'s attack missed.")
                else:
                    print("The " + enemy.name + "'s attack did " + str(eDamage) + " damage!")
                    self.p.currHP -= eDamage
                    if self.p.currHP <= 0:
                        print(self.p.name + " has 0 health remaining.")
                    else:
                        print(self.p.name + " has " + str(self.p.currHP) + " health remaining.")
        if (enemy.health <= 0 and self.p.currHP > 0):
            print(self.p.name + " has defeated the " + enemy.name)
            return
        else:
            print("The " + enemy.name + " has defeated " + self.p.name)
            print("Game Over")
            # Give them a chance to try again
            print("Would you like to try to fight again for 1 coin? 1. Yes 2. No")
            tryagain = self.playerChoice2("Yes", "No")
            if tryagain == "1":
                # The loss of currency can just be a punishment rather than a requirement
                self.p.currency -= 1
                self.p.currHP = self.p.maxHP
                enemy.health = enemy.maxHP
                self.battle(enemy)
                return
            elif tryagain == "2":
                exit()

    # Fix the play loop to loop itself after you complete a mission so you can choose the other ones
    # when looping we need it to ignore the missions we have already completed
    def play(self):
        print("Hello " + self.p.name + " you are a bounty hunter aboard your ship.\n\
You have 3 targets to go kill. Who would you like to kill first?\n\
1. Krag the Cruel 2. Badar the Barbaric 3. Jupiter the Giant...")

        mission = input()
        while (mission not in ["1", "2", "3"]):
            mission = input("Please enter a number for the target\n\
1. Krag the Cruel 2. Badar the Barbaric 3. Jupiter the Giant...")
        if (mission == "1"):
            self.krag()

        elif (mission == "2"):
            self.badar()

        else:
            self.jupiter()

# Krag
    def krag(self):
        print("Now going to planet Bababoeey to slay Krag the Cruel.")
        print("You land your ship in a parking bay in a packed city.\nBadar knows that he has a hit on him\
His goons are patrolling the town. What do you want to do?\n1. Fight the goons 2. Try to sneak past them.")

        choice = self.playerChoice2("Fight the goons", "Try to sneak past them.")
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
            option = input("1. Try to fight with fists 2. Run away")
            if option == "1":
                print("You decide to punch the goons with your fists.")
                self.battle(goon1)
                self.battle(goon2)
                # Reward them a knife if won
                print("You have won the fight, and therefore rewarded a knife.")
                self.p.items.append("Knife")

            elif option == "2":
                print("The goons now begin to chase you. You start running, and come across a pipe on the ground.")
                print("1. Pick up the pipe and attack 2. Continue to run away")

                option = None
                option = self.playerChoice2("Pick up the pipe and attack", "Continue to run away")

                if option == "1":
                    print("You decide to pick up the pipe, which increases your attack damage by 3 HP.")
                    self.p.items.append("Pipe")
                    self.p.attack += 3
                    print("You then start to attack the goons.")
                    self.battle(goon1)
                    self.battle(goon2)

                if option == "2":
                    print("You decide to keep running, but eventually get tired and therefore lose 2 HP.")
                    # Tell player that they lost HP due to fatigue from running
                    self.p.currHP -= 2
                    # If needed, you can tell player their current HP
                    print("You are now forced to fight the goons with your fists as you have nowhere else to go.")
                    self.battle(goon1)
                    self.battle(goon2)
                    # Tell player they got a knife
                    print("You have won the fight, and therefore rewarded a knife.")
                    self.p.items.append("Knife")




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
                self.battle(goon1)
                self.battle(goon2)

        # Everything past this point would apply to all winning scenarios
        print("You have successfully passed the goons and are now headed into the town.")
        print("You then spot Krag walking around, and quickly hide behind a structure.")

        # Add some kind of "background" by adding people the player can talk to
        option = None
        print("Beside you, there are town citizens. Would you like to speak with them to gather more \
information?\n 1. Yes 2. No")
        option = self.playerChoice2("Yes", "No")

        if option == "1":
            print("You go up to one young boy...\n")
            print("That freaky monster is taking over this whole town! What are you doing here?")
            option = None
            print("1. Explain that you are a bounty hunter and want to murder Krag \
2. Say that you are just there to visit family")
            option = self.playerChoice2("Explain that you are a bounty hunter and want to murder Krag",
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
        option = self.playerChoice2("Yes", "No")
        if option == "1":
            # If no money for armor
            if self.p.currency < 2:
                print("So you don't have those 2 coins, eh? Well, I want that annoying monster out of here, so I might \
aswell give you the armour for free")
                self.p.items.append(armour)
                self.p.maxHP += 10
                self.p.currHP += 10
            else:
                # If they have money for armour...
                self.p.currency -= 2
                self.p.maxHP += 10
                self.p.currHP += 10
                print("Thanks for coming! Good luck with your battle!")
        elif option == "2":
            print("Well, alright. Hopefully we will meet again!")

        print("You head outside and Krag instantly turns towards you. You step forward and decide to battle him.")
        krag = Enemy("Krag", 10, 8)
        self.battle(krag)

    def badar(self):
        print("Now going to planet Disco to slay Badar the Barbaric")

    def jupiter(self):
        print("Now going to planet Jupiter to slay Jupiter the Giant")


def main():
    print("You are playing \"Space Adventure\",\nPlease enter your character's name.")
    user = Player(input())
    theGame = Game(user)
    theGame.play()


main()
