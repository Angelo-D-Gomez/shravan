from player import *
from enemy import *

class Game:

    def __init__(self, player):
        self.p = player

    def play(self):
        print("Hello " + self.p.name + " you are a bounty hunter aboard your ship.\n\
You have 3 targets to go kill. Who would you like to kill first?\n\
1. Krag the Cruel 2. Badar the Barbaric 3. Jupiter the Giant...")
