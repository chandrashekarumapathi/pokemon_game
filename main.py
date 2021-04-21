import time
import sys
from random import randint


# Delay printing
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)


class Pokemon:
    def __init__(self, name: str, poke_type: str, moves: list, health=100, level=1):
        self.name = name
        self.type = poke_type
        self.moves = moves
        self.level = level
        self.health = health

    def show(self):
        print("Name: ", self.name)
        print("Type: ", self.type)
        print('Moves:')
        for i, x in enumerate(self.moves):
            print(f"{i}.", x)
        print("Level: ", self.level)
        print("Health: ", self.health)

    def show_moves(self):
        print('Moves:')
        for i, x in enumerate(self.moves):
            print(f"{i + 1}.", x)

    def choose_move(self):
        choice = int(input('Choose move\n'))
        for i in range(len(self.moves)):
            if choice == i + 1:
                print(f"{self.name} used {self.moves[i]}")

    def inflict_damage(self):
        damage = randint(1, 10)
        self.health = self.health - damage

    def attack(self):
        line = f"{self.name} turn to attack\n"
        delay_print(line)
        self.show_moves()
        self.choose_move()

    def show_health(self):
        line1 = f"{self.name} Health: {self.health}\n"
        delay_print(line1)

    def fight(self, pokemon2):
        print(f'Battle between {self.name} and {pokemon2.name}')
        while True:
            if self.health > 0 and pokemon2.health > 0:
                self.attack()
                pokemon2.inflict_damage()

                self.show_health()
                pokemon2.show_health()
                time.sleep(3)

                pokemon2.attack()
                self.inflict_damage()

                self.show_health()
                pokemon2.show_health()

            elif self.health <= 0:
                line3 = f"{pokemon2.name} is the winner!!!"
                delay_print(line3)
                break
            elif pokemon2.health <= 0:
                line4 = f"{self.name} is the winner!!!"
                delay_print(line4)
                break


pikachu = Pokemon(name='Pikachu', poke_type='Electric',
                  moves=['Quick Attack', 'Thundershock', 'Thunderbolt', 'Thunderpunch'], )
squirtle = Pokemon(name='Squirtle', poke_type='Water', moves=['Water Gun', 'Skull Bash', 'Bubble', 'Withdraw'])

pikachu.fight(pokemon2=squirtle)