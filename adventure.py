import time
import random

class enemy1():
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

class damage():
    def __init__(self, name, health, damage, ability, inventory):
        self.name = name
        self.health = health
        self.damage = damage
        self.ability = ability
        self.inventory = inventory

goblin = enemy1("johnny", 100, 10)
luke = damage("Luke", 100, 50, "Penguin Slap", [])




print("battle")
print(goblin.health - luke.damage)
goblin.health = goblin.health - luke.damage
if goblin.health <= 0:
    print(f"{luke.name} wins")
print(luke.health - goblin.damage)
luke.health = luke.health - goblin.damage
if luke.health <= 0:
    print(f"{goblin.name} wins")
print(goblin.health - luke.damage)
goblin.health = goblin.health - luke.damage
if goblin.health <= 0:
    print(f"{luke.name} wins")

print(luke.health)