import time
import random

class enemy1():
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

class damage():
    def __init__(self, health, damage, ability, inventory):
        self.health = health
        self.damage = damage
        self.ability = ability
        self.inventory = inventory

goblin = enemy1("johnny", 100, 10)
luke = damage("Luke", 100, 50, "Penguin Slap", [])

