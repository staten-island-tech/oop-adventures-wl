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

#Bunny is healer
class Bunny():
    def __init__(self, name, health, damage, ability, inventory):
        self.name = name
        self.health = health
        self.damage = damage
        self.ability = ability
        self.inventory = inventory

#Penguin is damage
class Penguin():
    def __init__(self, name, health, damage, ability, inventory):
        ability = [
            "Penguin Slap",
            "Penguin Punch",
            "Penguin Strike",
            "Penguin Beak Attack",
            "Penguin Stomp"
        ]
        self.name = name
        self.health = health
        self.damage = damage
        giveAbi = random.choice(ability)
        self.ability = giveAbi
        self.inventory = inventory

#battle

luke = Penguin("Luke", 100, 50, "", ["Vial"])
print(luke.__dict__)
print("hello")