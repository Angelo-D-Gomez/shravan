# make an enemy class
# enemy class needs to have HP, an attack value, we can use RNG to determine dodge chances
class Enemy:

    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.maxHP = health
        self.attack = attack
