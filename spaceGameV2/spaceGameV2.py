from player import *
from game import *

def main():
    print("You are playing \"Space Adventure\",\nPlease enter your character's name.")
    user = Player(input())
    theGame = Game(user)
    theGame.play()


main()
