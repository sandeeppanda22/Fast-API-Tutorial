from OOP.Enemy import *

zombie = Enemy()
zombie.type_of_enemy = 'Zombie'
zombie.talk()
zombie.walk_forward()
zombie.attack()

print(f'{zombie.type_of_enemy} has {zombie.health_points} health Points '
      f'and can do attack of {zombie.attack_damage}')