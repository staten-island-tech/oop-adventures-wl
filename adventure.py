import random
import time
#Wow an enemy
class Enemy():
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

#Cat is hypnotist
class Cat():
    def __init__(self, name, health, damage, shield, inventory):
        self.abilities = [
            {"abilityName":"Cat Meow","Damage":0,"Heal":25,},
            {"abilityName":"Cat Claws","Damage":50,"Heal":0,},
            {"abilityName":"Cat Eyes","Damage":random.randint(0,67),"Heal":0,},
            {"abilityName":"Angry Cat Attack","Damage":75,"Heal":0,}
        ]
        self.name = name
        self.health = health
        self.damage = damage
        self.shield = shield
        self.inventory = inventory

#Falcon is sniper
class Falcon():
    def __init__(self, name, health, damage, shield, inventory):
        self.abilities = [
            {"abilityName":"Falcon Dive","Damage":75,"Heal":0,},
            {"abilityName":"Falcon Feathers","Damage":20,"Heal":0,},
            {"abilityName":"Falcon Screech","Damage":50,"Heal":0,},
            {"abilityName":"Falcon Claw","Damage":40,"Heal":0,},
            {"abilityName":"Falcon Beak","Damage":40,"Heal":0,}
        ]
        self.name = name
        self.health = health
        self.damage = damage
        self.shield = shield
        self.inventory = inventory

#Snake is poison
class Snake():
    def __init__(self, name, health, damage, shield, inventory):
        self.abilities = [
            {"abilityName":"Snake Venom","Damage":33,"Heal":0,},
            {"abilityName":"Snake Crush","Damage":40,"Heal":0,},
            {"abilityName":"Snake Fangs","Damage":40,"Heal":0,},
            {"abilityName":"Snake Hiss","Damage":20,"Heal":10,}
        ]
        self.name = name
        self.health = health
        self.damage = damage
        self.shield = shield
        self.inventory = inventory

#Frog is support
class Frog():
    def __init__(self, name, health, damage, shield, inventory):
        self.abilities = [
            {"abilityName":"Frog Boost","Damage":33,"Heal":0,},
            {"abilityName":"Frog Assist","Damage":20,"Heal":30},
            {"abilityName":"Frog Vial","Damage":10,"Heal":random.randint(50,67),}
        ]
        self.name = name
        self.health = health
        self.damage = damage
        self.shield = shield
        self.inventory = inventory

#Shark is tank
class Shark():
    def __init__(self, name, health, damage, shield, inventory):
        self.abilities = [
            {"abilityName":"Shark Attack","Damage":50,"Heal":0,},
            {"abilityName":"Shark Fin","Damage":45,"Heal":30},
            {"abilityName":"Shark Tail Swing","Damage":25,"Heal":25,},
            {"abilityName":"Shark Skin","Damage":33,"Heal":0,},
            {"abilityName":"Shark Teeth","Damage":67,"Heal":1}
        ]
        self.name = name
        self.health = health
        self.damage = damage
        self.shield = shield
        self.inventory = inventory

#Bunny is Healer
class Bunny():
    def __init__(self, name, health, damage, shield, inventory):
        self.abilities = [
            {"abilityName":"Bunny Heal","Damage":0,"Heal":50,},
            {"abilityName":"Bunny Shield","Damage":25,"Heal":30},
            {"abilityName":"Bunny Protection","Damage":30,"Heal":25,}
        ]
        self.name = name
        self.health = health
        self.damage = damage
        self.shield = shield
        self.inventory = inventory

#Penguin is damage
class Penguin():
    def __init__(self, name, health, damage, shield, inventory):
        self.abilities = [
            {"abilityName":"Penguin Slap","Damage":44,"Heal":0,},
            {"abilityName":"Penguin Punch","Damage":65,"Heal":0,},
            {"abilityName":"Penguin Slide","Damage":5,"Heal":50,},
            {"abilityName":"Penguin Beak Attack","Damage":35,"Heal":0,},
            {"abilityName":"Penguin Stomp","Damage":random.randint(25,50),"Heal":1,}
        ]
        self.name = name
        self.health = health
        self.damage = damage
        self.shield = shield
        self.inventory = inventory

while True:
    classify = input("What class would you like to be? Damage, Tank, Healer, Support, Poison, Sniper, Hypnotist. ").lower()
    if classify == ("damage"):
        naming = input("What is your name? ")
        character = Penguin(naming, 100, 10, 0, [])
        break
    if classify == ("tank"):
        naming = input("What is your name? ")
        character = Shark(naming, 100, 10, 0, [])
        break
    elif classify == ("Healer"):
        naming = input("What is your name? ")
        character = Bunny(naming, 100, 10, 0, [])
        break
    elif classify == ("support"):
        naming = input("What is your name? ")
        character = Frog(naming, 100, 10, 0, [])
        break
    elif classify == ("poison"):
        naming = input("What is your name? ")
        character = Snake(naming, 100, 10, 0, [])
        break
    elif classify == ("sniper"):
        naming = input("What is your name? ")
        character = Falcon(naming, 100, 10, 0, [])
        break
    elif classify == ("hypnotist"):
        naming = input("What is your name? ")
        character = Cat(naming, 100, 10, 0, [])
        break
    else:
        print("Class not found")

print(character.__dict__)
time.sleep(2)

print("Game starting...")
time.sleep(2)
goblin = Enemy("Goblin", 75, 10)

def battle():
    print(f"{character.name} is now fighting {goblin.name}!")
    time.sleep(2)

    while character.health > 0 and goblin.health > 0:
        print(f"{character.name} is now attacking!")
        time.sleep(2)
        print(f"What will {character.name} do? ")
        print("1. Use normal attack")
        print("2. Use item in inventory")
        print("3. Use ability")
        print("4. Run away")
        action = int(input("Write 1, 2, 3, or 4: "))
        if action == 1:
            print(f"{character.name} did {character.damage} damage to {goblin.name}!")
            goblin.health = goblin.health - character.damage
            time.sleep(2)
            print(f"{goblin.name} is now at {goblin.health} health.")
            if goblin.health <= 0:
                print(f"{goblin.name} has been defeated!")
                return

        elif action == 2:
            if not character.inventory:
                print("Inventory is still in the works and will come out in v2.0.")

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
            print(f"{goblin.name} is now at {goblin.health} health.")
            time.sleep(2)
            print(f"{character.name} is now at {character.health} health.")
            if goblin.health <= 0:
                print(f"{goblin.name} has been defeated!")
                return

        elif action == 4:
            print(f"{character.name} ran away!")
            return

        time.sleep(3)
        print(f"{goblin.name} is now attacking!")
        time.sleep(2)
        print(f"{goblin.name} did {goblin.damage} damage to {character.name}!")
        character.health = character.health - goblin.damage
        time.sleep(2)
        print(f"{character.name} is now at {character.health} health.")
        if character.health <= 0:
            print(f"{character.name} has been defeated!")
            return
        
battle()