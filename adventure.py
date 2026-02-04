import random
import time
#add levels, chests, equippables, more enemies, fix random randint somehow

#Wow an enemy
class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

class Character:
    def __init__(self, name, health, damage, shield, inventory):
        self.name = name
        self.health = health
        self.damage = damage
        self.shield = shield
        self.inventory = inventory
        self.abilities = []

# Cat is hypnotist
class Cat(Character):
    def __init__(self, name, health, damage, shield, inventory):
        super().__init__(name, health, damage, shield, inventory)
        self.abilities = [
            {"abilityName": "Cat Meow", "Damage": 0, "Heal": 25},
            {"abilityName": "Cat Eyes", "Damage": random.randint(0, 40), "Heal": 5},
            {"abilityName": "Cat Claws", "Damage": 50, "Heal": 0},
            {"abilityName": "Angry Cat Attack", "Damage": random.randint(50, 75), "Heal": 0}
        ]

#Falcon is sniper
class Falcon(Character):
    def __init__(self, name, health, damage, shield, inventory):
        super().__init__(name, health, damage, shield, inventory)
        self.abilities = [
            {"abilityName": "Falcon Dive", "Damage": 75, "Heal": 0},
            {"abilityName": "Falcon Feathers", "Damage": 20, "Heal": 0},
            {"abilityName": "Falcon Screech", "Damage": 35, "Heal": 0},
            {"abilityName": "Falcon Claw", "Damage": 40, "Heal": 0},
            {"abilityName": "Falcon Beak", "Damage": 50, "Heal": 0}
        ]

#Snake is poison
#ADD PERIODIC POISON
class Snake(Character):
    def __init__(self, name, health, damage, shield, inventory):
        super().__init__(name, health, damage, shield, inventory)
        self.abilities = [
            {"abilityName": "Snake Venom", "Damage": 33, "Heal": 0},
            {"abilityName": "Snake Crush", "Damage": 50, "Heal": 0},
            {"abilityName": "Snake Fangs", "Damage": 30, "Heal": 0},
            {"abilityName": "Snake Hiss", "Damage": 20, "Heal": 15}
        ]

#Frog is support
#ADD PERIODIC HEALS
#frog boost boosts dmg, frog assist boosts hp or shield
class Frog(Character):
    def __init__(self, name, health, damage, shield, inventory):
        super().__init__(name, health, damage, shield, inventory)
        self.abilities = [
            {"abilityName": "Frog Boost", "Damage": 20, "Heal": 5},
            {"abilityName": "Frog Assist", "Damage": 5, "Heal": 20},
            {"abilityName": "Frog Vial", "Damage": 10, "Heal": random.randint(25, 75)}
        ]

#Shark is tank
class Shark(Character):
    def __init__(self, name, health, damage, shield, inventory):
        super().__init__(name, health, damage, shield, inventory)
        self.abilities = [
            {"abilityName": "Shark Attack", "Damage": 50, "Heal": 0},
            {"abilityName": "Shark Fin", "Damage": 40, "Heal": 15},
            {"abilityName": "Shark Tail Swing", "Damage": 25, "Heal": 15},
            {"abilityName": "Shark Skin", "Damage": 20, "Heal": 0},
            {"abilityName": "Shark Teeth", "Damage": 50, "Heal": 10}
        ]

#Bunny is healer
class Bunny(Character):
    def __init__(self, name, health, damage, shield, inventory):
        super().__init__(name, health, damage, shield, inventory)
        self.abilities = [
            {"abilityName": "Bunny Heal", "Damage": 0, "Heal": 50},
            {"abilityName": "Bunny Shield", "Damage": 10, "Heal": 30},
            {"abilityName": "Bunny Protection", "Damage": 20, "Heal": 25}
        ]

#Penguin is damage
class Penguin(Character):
    def __init__(self, name, health, damage, shield, inventory):
        super().__init__(name, health, damage, shield, inventory)
        self.abilities = [
            {"abilityName": "Penguin Slap", "Damage": 35, "Heal": 0},
            {"abilityName": "Penguin Punch", "Damage": 50, "Heal": 0},
            {"abilityName": "Penguin Slide", "Damage": 5, "Heal": 40},
            {"abilityName": "Penguin Beak Attack", "Damage": 25, "Heal": 10},
            {"abilityName": "Penguin Stomp", "Damage": random.randint(15, 40), "Heal": 0}
        ]

while True:
    classify = input("What class would you like to be? Damage, Tank, Healer, Support, Poison, Sniper, Hypnotist. ").lower()
    if classify == ("damage"):
        naming = input("What is your name? ")
        character = Penguin(naming, 175, 30, 0, [])
        break
    if classify == ("tank"):
        naming = input("What is your name? ")
        character = Shark(naming, 250, 10, 10, [])
        break
    elif classify == ("healer"):
        naming = input("What is your name? ")
        character = Bunny(naming, 200, 10, 0, [])
        break
    elif classify == ("support"):
        naming = input("What is your name? ")
        character = Frog(naming, 200, 10, 0, [])
        break
    elif classify == ("poison"):
        naming = input("What is your name? ")
        character = Snake(naming, 200, 15, 0, [])
        break
    elif classify == ("sniper"):
        naming = input("What is your name? ")
        character = Falcon(naming, 175, 25, 0, [])
        break
    elif classify == ("hypnotist"):
        naming = input("What is your name? ")
        character = Cat(naming, 200, random.randint(5, 25), 0, [])
        break
    else:
        print("Class not found")

print(character.__dict__)
time.sleep(2)

print("Game starting...")
time.sleep(2)
goblin = Enemy("Goblin", 300, 25)

def battle():
    print(f"{character.name} is now fighting {goblin.name}!")
    time.sleep(2)

    while character.health > 0 and goblin.health > 0:
        print(f"{character.name} is now attacking!")
        time.sleep(2)
        print(f"What will {character.name} do? ")
        time.sleep(1)
        print("1. Use normal attack")
        time.sleep(0.5)
        print("2. Use item in inventory")
        time.sleep(0.5)
        print("3. Use ability")
        time.sleep(0.5)
        print("4. Run away")
        action = int(input("Write 1, 2, 3, or 4: "))
        if action == 1:
            print(f"{character.name} did {character.damage} damage to {goblin.name}!")
            goblin.health = goblin.health - character.damage
            time.sleep(2)
            if goblin.health <= 0:
                goblin.health = 0
            print(f"{goblin.name} is now at {goblin.health} health.")
            if goblin.health <= 0:
                print(f"{goblin.name} has been defeated!")
                return

        elif action == 2:
            if not character.inventory:
                print("Inventory is still in the works and will come out in v2.0.")
                continue

        elif action == 3:
            for i, ability in enumerate(character.abilities, start=1):
                print(f"{i}. {ability['abilityName']} (Damage: {ability['Damage']}, Heal: {ability['Heal']})")

            chooseability = int(input("Which ability would you like to use? ")) - 1
            chosen = character.abilities[chooseability]

            goblin.health -= chosen["Damage"]
            character.health += chosen["Heal"]

            print(f"{character.name} used {chosen['abilityName']}!")
            time.sleep(2)
            print(f"{character.name} did {chosen['Damage']} damage to {goblin.name}!")
            time.sleep(2)
            if goblin.health <= 0:
                goblin.health = 0
            print(f"{goblin.name} is now at {goblin.health} health.")
            time.sleep(2)
            print(f"{character.name} is now at {character.health} health.")
            time.sleep(1)
            if goblin.health <= 0:
                print(f"{goblin.name} has been defeated!")
                return

        elif action == 4:
            print(f"{character.name} ran away!")
            return
        
        else: 
            print("This is not an action.")
            continue
        
        time.sleep(2)
        print(" ")
        print(f"{goblin.name} is now attacking!")
        time.sleep(2)
        print(f"{goblin.name} did {goblin.damage} damage to {character.name}!")
        character.health = character.health - goblin.damage
        time.sleep(2)
        print(f"{character.name} is now at {character.health} health.")
        print(" ")
        time.sleep(2)
        if character.health <= 0:
            print(f"{character.name} has been defeated!")
            return
        
battle()