import time
import random

class Enemy1():
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

class Poison():
    def __init__(self, name, health, damage, ability, inventory):
        self.name = name
        self.health = health
        self.damage = damage
        self.ability = ability
        self.inventory = inventory

class Support():
    def __init__(self, name, health, damage, ability, inventory):
        self.name = name
        self.health = health
        self.damage = damage
        self.ability = ability
        self.inventory = inventory

class Tank():
    def __init__(self, name, health, damage, ability, inventory):
        self.name = name
        self.health = health
        self.damage = damage
        self.ability = ability
        self.inventory = inventory

class Healer():
    def __init__(self, name, health, damage, ability, inventory):
        self.name = name
        self.health = health
        self.damage = damage
        self.ability = ability
        self.inventory = inventory

class Damage():
    def __init__(self, name, health, damage, ability, inventory):
        self.name = name
        self.health = health
        self.damage = damage
        self.ability = ability
        self.inventory = inventory
        number = [0, 1, 2, 3, 4]
        giveAbi = random.choice(number)
        if giveAbi == ("0"):
            self.ability = "Penguin Slap"
        elif giveAbi == ("1"):
            self.ability = "Penguin Punch"
        elif giveAbi == ("2"):
            self.ability = "Penguin Strike"
        elif giveAbi == ("3"):
            self.ability = "Penguin Beak Attack"
        elif giveAbi == ("4"):
            self.ability = "Penguin Stomp"

luke = Damage("Luke", 100, 50, "", ["Vial"])
print(luke.__dict__)
print("hello")