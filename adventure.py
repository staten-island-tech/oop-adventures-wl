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



number = [0, 1, 2, 3, 4]
luke = damage("Luke", 100, 50, random.choice(number), ["vial"])
if number == ("0", "1", "2", "3", "4"):
    luke.ability == ("penguin slap")
print(luke.__dict__)