from player import *
from krag import krag
from jupiter import jupiter
from badar import badar


class Game:

    def __init__(self, player):
        self.p = player

    def playerChoice2(self, choice1, choice2):
        choice = input()
        while choice not in ["1", "2"]:
            choice = input("Please enter the number of your choice.\n\
1. " + choice1 + " 2. " + choice2)
        return choice    

    def play(self):
        print("Hello " + self.p.name + " you are a bounty hunter aboard your ship.\n\
You have 3 targets to go kill. Who would you like to kill first?\n\
1. Krag the Cruel 2. Badar the Barbaric 3. Jupiter the Giant...")

        mission = input()
        while mission not in ["1", "2", "3"]:
            mission = input("Please enter a number for the target\n\
1. Krag the Cruel 2. Badar the Barbaric 3. Jupiter the Giant...")
        if mission == "1":
            krag(self, self.p)

        elif mission == "2":
            badar(self, self.p)

        else:
            jupiter(self, self.p)
