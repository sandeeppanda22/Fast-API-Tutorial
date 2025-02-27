from OOP.Enemy import *

enemy = Enemy()
enemy.type_of_enemy = 'Zombie'

print(f'{enemy.type_of_enemy} has {enemy.health_points} health Points '
      f'and can do attack of {enemy.attack_damage}')