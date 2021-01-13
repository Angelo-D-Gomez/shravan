from random import randint


def battle(game, p, e):
    while p.currHP > 0 and e.health > 0:
        firstStrike = randint(0, 1)
        # This is if enemy attacks first
        if firstStrike == 0:
            print("The " + e.name + " attacks first.")
            eDamage = randint(0, e.attack)
            if eDamage == 0:
                print("The " + e.name + "'s attack missed.")
            else:
                print("The " + e.name + "'s attack did " + str(eDamage) + " damage!")
                p.currHP -= eDamage
                if p.currHP <= 0:
                    print(p.name + " has 0 health remaining.")
                    break
                else:
                    print(p.name + " has " + str(p.currHP) + " health remaining.")

            pDamage = randint(0, p.attack)
            if pDamage == 0:
                print(p.name + "'s attack missed.")
            else:
                e.health -= pDamage
                print(p.name + " attacks and does " + str(pDamage) + " damage.")

        else:
            print(p.name + " attacks first!")
            pDamage = randint(0, p.attack)
            if pDamage == 0:
                print(p.name + "'s attack missed.")
            else:
                e.health -= pDamage
                print(p.name + " attacks and does " + str(pDamage) + " damage.")
                if e.health <= 0:
                    break
            eDamage = randint(0, e.attack)
            if eDamage == 0:
                print("The " + e.name + "'s attack missed.")
            else:
                print("The " + e.name + "'s attack did " + str(eDamage) + " damage!")
                p.currHP -= eDamage
                if p.currHP <= 0:
                    print(p.name + " has 0 health remaining.")
                else:
                    print(p.name + " has " + str(p.currHP) + " health remaining.")

    if e.health <= 0 and p.currHP > 0:
        print(p.name + " has defeated the " + e.name)
        return
    else:
        print("The " + e.name + " has defeated " + p.name)
        print("Game Over")

        # Give them a chance to try again
        print("Would you like to try to fight again for 1 coin? 1. Yes 2. No")
        tryagain = game.playerChoice2("Yes", "No")
        if tryagain == "1":
            # The loss of currency can just be a punishment rather than a requirement
            p.currency -= 1
            p.currHP = self.p.maxHP
            e.health = enemy.maxHP
            battle(game, p, e)
            return
        elif tryagain == "2":
            exit()
