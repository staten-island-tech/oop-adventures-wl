import time
import random

class enemy1():
    def __init__(self, health, damage):
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

while True:
    classify = input("What class would you like to be? Damage, Tank, Healer, Support, Poison, Sniper, Hypnotist. ").lower()
    if classify == ("damage"):
        naming = input("What is your name? ")
        luke = Penguin(naming, 100, 10, 0, "", [""])
        break
    if classify == ("tank"):
        naming = input("What is your name? ")
        luke = Shark(naming, 100, 10, 0, "", [""])
        break
    elif classify == ("healer"):
        naming = input("What is your name? ")
        luke = Bunny(naming, 100, 10, 0, "", [""])
        break
    elif classify == ("support"):
        naming = input("What is your name? ")
        luke = Frog(naming, 100, 10, 0, "", [""])
        break
    elif classify == ("poison"):
        naming = input("What is your name? ")
        luke = Snake(naming, 100, 10, 0, "", [""])
        break
    elif classify == ("sniper"):
        naming = input("What is your name? ")
        luke = Falcon(naming, 100, 10, 0, "", [""])
        break
    elif classify == ("hypnotist"):
        naming = input("What is your name? ")
        luke = Cat(naming, 100, 10, 0, "", [""])
        break
    else:
        print("Class not found")

print(luke.__dict__)

print("Game starting...")
time.sleep(2)
goblin = Enemy("Goblin", 75, 10)

def battle():
    print(f"{luke.name} is now fighting {goblin.name}!")
    time.sleep(2)
    print(f"{luke.name} is now attacking!")
    time.sleep(2)
    print(f"What will {luke.name} do? ")
    print("1. Use normal attack")
    print("2. Use item in inventory")
    print("3. Use ability")
    print("4. Run away")
    action = int(input("Write 1, 2, 3, or 4: "))
    if action == 1:
        print(f"{luke.name} did {luke.damage} to {goblin.name}!")
        goblin.health = goblin.health - luke.damage
        time.sleep(2)
        print(f"{goblin.name} is now at {goblin.health}.")
        if goblin.health <= 0:
            print(f"{goblin.name} has been defeated!")
            
    elif action == 2:
        if not luke.inventory:
            print("There is nothing in your inventory.")
    
    elif action == 3:
        for i, ability in enumerate(luke.abilities, start = 1):
            print(f"{i}. {ability}")
        chooseability = int(input("Which ability would you like to use? "))
        if chooseability == 1:
            print("cool")
    
    elif action == 4:
        print("I'm going to roast you.")

    time.sleep(3)
    print(f"{goblin.name} is now attacking!")
    time.sleep(2)
    print(f"{goblin.name} did {goblin.damage} to {luke.name}!")
    luke.health = luke.health - goblin.damage
    time.sleep(2)
    print(f"{luke.name} is now at {luke.health}.")
    if luke.health <= 0:
        print(f"{luke.name} has been defeated!")
        

battle()