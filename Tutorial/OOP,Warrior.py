import random
import math

class Warrior:
    def __init__(self,name='Warrior',health=0,attackmax=0,blockmax=0):
        self.name = name
        self.health = health
        self.attackmax = attackmax
        self.blockmax = blockmax

    def attack(self):
        attkamt = self.attackmax * (random.random() + .5)
        return attkamt
    def block(self):
        blockamt = self.blockmax * (random.random() + .5)
        return blockamt



class Battle:
    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == 'Game Over':
                print('Game Over')
                break
            if self.getAttackResult(warrior2, warrior1) == 'Game Over':
                print('Mike Sucks')
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAAttkAmt = warriorA.attack()
        warriorBBlockAmt = warriorB.block()
        damage2WarriorB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)
        warriorB.health = warriorB.health - damage2WarriorB

        print('{} attacks {} and deals {} damage'.format(warriorA.name,warriorB.name, damage2WarriorB))

        print('{} is down to {} health'.format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print('{} has Died and {} is Victorious'.format(warriorB.name, warriorA.name))
            return 'Game Over'
        else:
            return 'Fight Again'

def main():
    firstwarrior = Warrior('Aaron', 50,20,10)
    secondwarrior = Warrior('Mike', 50,20,10)
    battle = Battle()
    battle.startFight(firstwarrior, secondwarrior)

main()
