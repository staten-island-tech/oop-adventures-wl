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
        random.choice(number)
        if random.choice == ("0", "1", "2", "3", "4"):
            ability == "penguin slap"

luke = damage("Luke", 100, 50, "", ["Vial"])
print(luke.__dict__)