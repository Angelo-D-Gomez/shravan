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
