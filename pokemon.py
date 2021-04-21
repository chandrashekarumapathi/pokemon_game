import time
import numpy as np
import sys


# Delay printing
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.5)


# Lets create a Class
class Pokemon:
    def __init__(self, name, type, moves, EVs, health='===================='):
        self.name = name
        self.type = type
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20

    def show_info_before_battle(self, Pokemon2):
        print("-----POKEMONE BATTLE-----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3 * (1 + np.mean([self.attack, self.defense])))
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3 * (1 + np.mean([Pokemon2.attack, Pokemon2.defense])))
        time.sleep(2)

    def type_advantages(self, Pokemon2):
        version = ['Fire', 'Water', 'Grass']
        for i, k in enumerate(version):
            if self.type == k and Pokemon2.type == k:
                self.string_1_attack = '\nIts not very effective...'
                self.string_2_attack = '\nIts not very effective...'

            # Pokemon2 is STRONG
            if Pokemon2.type == version[(i + 1) % 3]:
                Pokemon2.attack *= 2
                Pokemon2.defense *= 2
                self.attack /= 2
                self.defense /= 2
                self.string_1_attack = '\nIts not very effective...'
                self.string_2_attack = '\nIts SUPER effective!'

            # Pokemon2 is WEAK
            if Pokemon2.type == version[(i + 2) % 3]:
                self.attack *= 2
                self.defense *= 2
                Pokemon2.attack /= 2
                Pokemon2.defense /= 2
                self.string_1_attack = '\nIts SUPER effective!'
                self.string_2_attack = '\nIts not very effective...'

    def actual_fighting(self, Pokemon2):
        while (self.bars > 0) and (Pokemon2.bars > 0):
            print(f"\n{self.name}\t\tHEALTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}\n")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i}.", x)

            index = int(input('Pick a move: '))
            delay_print(f"\n{self.name} used {self.moves[index]}!")
            time.sleep(1)
            delay_print(self.string_1_attack)






