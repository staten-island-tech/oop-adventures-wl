import time
import random

class Enemy1():
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

#Falcon is sniper
class Falcon():
    def __init__(self, name, health, damage, shield, ability, inventory):
        ability = [
            "Falcon Dive",
            "Falcon Feathers",
            "Falcon Screech",
            "Falcon Claw",
            "Falcon Beak"
        ]
        self.name = name
        self.health = health
        self.damage = damage
        self.shield = shield
        self.ability = ability
        self.inventory = inventory

#Snake is poison
class Snake():
    def __init__(self, name, health, damage, shield, ability, inventory):
        ability = [
            "Snake Venom",
            "Snake Crush",
            "Snake Fangs",
            "Snake Hiss"
        ]
        self.name = name
        self.health = health
        self.damage = damage
        self.shield = shield
        self.ability = ability
        self.inventory = inventory

#Frog is support
class Frog():
    def __init__(self, name, health, damage, shield, ability, inventory):
        ability = [
            "Frog Boost", #Raises damage
            "Frog Assist", #Frog also attacks
            "Frog Vial" #Raises health
        ]
        self.name = name
        self.health = health
        self.damage = damage
        self.shield = shield
        self.ability = ability
        self.inventory = inventory

#Shark is tank
class Shark():
    def __init__(self, name, health, damage, shield, ability, inventory):
        ability = [
            "Shark Attack",
            "Shark Fin",
            "Shark Tail Swing",
            "Shark Skin",
            "Shark Teeth"
        ]
        self.name = name
        self.health = health
        self.damage = damage
        self.shield = shield
        self.ability = ability
        self.inventory = inventory

#Bunny is healer
class Bunny():
    def __init__(self, name, health, damage, shield, ability, inventory):
        ability = [
            "Bunny Heal",
            "Bunny Shield",
            "Bunny Protection"
        ]
        self.name = name
        self.health = health
        self.damage = damage
        self.shield = shield
        self.ability = ability
        self.inventory = inventory

#Penguin is damage
class Penguin():
    def __init__(self, name, health, damage, shield, ability, inventory):
        ability = [
            "Penguin Slap",
            "Penguin Punch",
            "Penguin Slide",
            "Penguin Beak Attack",
            "Penguin Stomp"
        ]
        self.name = name
        self.health = health
        self.damage = damage
        self.shield = shield
        self.ability = ability
        self.inventory = inventory

luke = Penguin("Luke", 100, 50, 0, "", [""])
print(luke.__dict__)
print("hello")