from player import *
from krag import krag
from jupiter import jupiter
from badar import badar


class Game:



    def __init__(self, player):
        self.p = player
        self.missionopt = [["1", "2", "3"],
                         ["Krag the Cruel", "Badar the Barbaric", "Jupiter the Giant"]]

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
            self.p = krag(self, self.p)
            self.missionopt[0].pop(2)
            self.missionopt[1].pop(0)

        elif mission == "2":
            self.p = badar(self, self.p)
            self.missionopt[0].pop(2)
            self.missionopt[1].pop(1)

        # Add return statement in badar and jupiter
        else:
            self.p = jupiter(self, self.p)
            self.missionopt[0].pop(2)
            self.missionopt[1].pop(2)

        print("Choose your next mission.")
        print("1. " + self.missionopt[1][0] + " 2. " + self.missionopt[1][1])
        # Temporarily don't use playerChoice2
        mission = input()
        while mission not in ["1", "2"]:
            mission = input("Please enter a number for the target\n\
1. " + self.missionopt[1][0] + " 2. " + self.missionopt[1][1])
        if mission == "1":
            pass
        elif mission == "2":
            pass

        # Note: Once only one mission remains,
        # make simple prompt for player to continue onto next mission


