import time
import random

#Wow an enemy
class Enemy():
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

#Cat is hypnotist
class Cat():
    def __init__(self, name, health, damage, shield, abilities, inventory):
        abilities = [
            "Cat Meow",
            "Cat Claws",
            "Cat Eyes",
            "Angry Cat Attack"
        ]
        self.name = name
        self.health = health
        self.damage = damage
        self.shield = shield
        self.abilities = abilities
        self.inventory = inventory

#Falcon is sniper
class Falcon():
    def __init__(self, name, health, damage, shield, abilities, inventory):
        abilities = [
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
        self.abilities = abilities
        self.inventory = inventory

#Snake is poison
class Snake():
    def __init__(self, name, health, damage, shield, abilities, inventory):
        abilities = [
            "Snake Venom",
            "Snake Crush",
            "Snake Fangs",
            "Snake Hiss"
        ]
        self.name = name
        self.health = health
        self.damage = damage
        self.shield = shield
        self.abilities = abilities
        self.inventory = inventory

#Frog is support
class Frog():
    def __init__(self, name, health, damage, shield, abilities, inventory):
        abilities = [
            "Frog Boost", #Raises damage
            "Frog Assist", #Frog also attacks
            "Frog Vial" #Raises health
        ]
        self.name = name
        self.health = health
        self.damage = damage
        self.shield = shield
        self.abilities = abilities
        self.inventory = inventory

#Shark is tank
class Shark():
    def __init__(self, name, health, damage, shield, abilities, inventory):
        abilities = [
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
        self.abilities = abilities
        self.inventory = inventory

#Bunny is healer
class Bunny():
    def __init__(self, name, health, damage, shield, abilities, inventory):
        abilities = [
            "Bunny Heal",
            "Bunny Shield",
            "Bunny Protection"
        ]
        self.name = name
        self.health = health
        self.damage = damage
        self.shield = shield
        self.abilities = abilities
        self.inventory = inventory

#Penguin is damage
class Penguin():
    def __init__(self, name, health, damage, shield, abilities, inventory):
        abilities = [
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
        self.abilities = abilities
        self.inventory = inventory


classify = input("What class would you like to be? Damage, Tank, Healer, Support, Poison, Sniper, Hypnotist. ")
if classify == ("Damage") or ("damage"):
    naming = input("What is your name? ")
    luke = Penguin(naming, 100, 10, 0, "", [""])
if classify == ("Tank") or ("tank"):
    naming = input("What is your name? ")
    luke = Shark(naming, 100, 10, 0, "", [""])
elif classify == ("Healer") or ("healer"):
    naming = input("What is your name? ")
    luke = Bunny(naming, 100, 10, 0, "", [""])
elif classify == ("Support") or ("support"):
    naming = input("What is your name? ")
    luke = Frog(naming, 100, 10, 0, "", [""])
elif classify == ("Poison") or ("poison"):
    naming = input("What is your name? ")
    luke = Snake(naming, 100, 10, 0, "", [""])
elif classify == ("Sniper") or ("sniper"):
    naming = input("What is your name? ")
    luke = Falcon(naming, 100, 10, 0, "", [""])
elif classify == ("Hypnotist") or ("hypnotist"):
    naming = input("What is your name? ")
    luke = Cat(naming, 100, 10, 0, "", [""])
else:
    print("Class not found")

goblin = Enemy("Goblin", 75, 10)
print(luke.__dict__)


def battle():
    print(f"{luke.name} is now fighting {goblin.name}!")
    time.sleep(1)
    action = input("What will you do? ")
    print("1. Use normal attack")
    

battle()