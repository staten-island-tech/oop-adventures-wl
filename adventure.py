import random
import time
#add levels, chests, equippables, more enemies, fix random randint somehow

messages = [
    "Welcome to Anifighter RPG!",
    "This game is about you fighting monsters and slowly getting more powerful,",
    "finally being able to defeat the last boss.",
    "I would say similar stuff to those game ads you see online,",
    "but that's just way too cringe to put here.",
    "Anyways, enjoy this game!"
]
for line in messages:
    time.sleep(2)
    print(line)

time.sleep(2)

#Wow an enemy

class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

class TutorialGoblin(Enemy):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.name = name
        self.health = health
        self.damage = damage

class Character:
    def __init__(self, name, health, damage, shield, inventory, equipinven, equippables, classed, gold):
        self.name = name
        self.health = health
        self.damage = damage
        self.shield = shield
        self.inventory = inventory
        self.abilities = []
        self.equipinven = equipinven
        self.equippables = equippables
        self.classed = classed
        self.gold = gold

# Cat is hypnotist
class Cat(Character):
    def __init__(self, name, health, damage, shield, inventory, equipinven, equippables, classed, gold):
        super().__init__(name, health, damage, shield, inventory, equipinven, equippables, classed, gold)
        self.abilities = [
            {"abilityName": "Cat Meow", "Damage": 0, "Heal": 25},
            {"abilityName": "Cat Eyes", "Damage": random.randint(0, 40), "Heal": 5},
            {"abilityName": "Cat Claws", "Damage": 50, "Heal": 0},
            {"abilityName": "Angry Cat Attack", "Damage": random.randint(50, 75), "Heal": 0}
        ]

#Falcon is sniper
class Falcon(Character):
    def __init__(self, name, health, damage, shield, inventory, equipinven, equippables, classed, gold):
        super().__init__(name, health, damage, shield, inventory, equipinven, equippables, classed, gold)
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
    def __init__(self, name, health, damage, shield, inventory, equipinven, equippables, classed, gold):
        super().__init__(name, health, damage, shield, inventory, equipinven, equippables, classed, gold)
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
    def __init__(self, name, health, damage, shield, inventory, equipinven, equippables, classed, gold):
        super().__init__(name, health, damage, shield, inventory, equipinven, equippables, classed, gold)
        self.abilities = [
            {"abilityName": "Frog Boost", "Damage": 20, "Heal": 5},
            {"abilityName": "Frog Assist", "Damage": 5, "Heal": 20},
            {"abilityName": "Frog Vial", "Damage": 10, "Heal": random.randint(25, 75)}
        ]

#Shark is tank
class Shark(Character):
    def __init__(self, name, health, damage, shield, inventory, equipinven, equippables, classed, gold):
        super().__init__(name, health, damage, shield, inventory, equipinven, equippables, classed, gold)
        self.abilities = [
            {"abilityName": "Shark Attack", "Damage": 50, "Heal": 0},
            {"abilityName": "Shark Fin", "Damage": 40, "Heal": 15},
            {"abilityName": "Shark Tail Swing", "Damage": 25, "Heal": 15},
            {"abilityName": "Shark Skin", "Damage": 20, "Heal": 0},
            {"abilityName": "Shark Teeth", "Damage": 50, "Heal": 10}
        ]

#Bunny is healer
class Bunny(Character):
    def __init__(self, name, health, damage, shield, inventory, equipinven, equippables, classed, gold):
        super().__init__(name, health, damage, shield, inventory, equipinven, equippables, classed, gold)
        self.abilities = [
            {"abilityName": "Bunny Heal", "Damage": 0, "Heal": 50},
            {"abilityName": "Bunny Shield", "Damage": 10, "Heal": 30},
            {"abilityName": "Bunny Protection", "Damage": 20, "Heal": 25}
        ]

#Penguin is damage
class Penguin(Character):
    def __init__(self, name, health, damage, shield, inventory, equipinven, equippables, classed, gold):
        super().__init__(name, health, damage, shield, inventory, equipinven, equippables, classed, gold)
        self.abilities = [
            {"abilityName": "Penguin Slap", "Damage": 35, "Heal": 0},
            {"abilityName": "Penguin Punch", "Damage": 50, "Heal": 0},
            {"abilityName": "Penguin Slide", "Damage": 5, "Heal": 40},
            {"abilityName": "Penguin Beak Attack", "Damage": 25, "Heal": 10},
            {"abilityName": "Penguin Stomp", "Damage": random.randint(15, 40), "Heal": 0}
        ]
    def __add__(self, gold):
        if isinstance(gold, int):
            return Penguin(self.value + gold)
        elif isinstance(gold, Penguin):
            return Penguin(self.value + gold.value)

while True:
    classify = input("What class would you like to be? Damage, Tank, Healer, Support, Poison, Sniper, Hypnotist. ").lower()
    if classify == ("damage"):
        naming = input("What is your name? ")
        character = Penguin(naming, 175, 30, 0, [], [], [], "Penguin", 0)
        break
    if classify == ("tank"):
        naming = input("What is your name? ")
        character = Shark(naming, 250, 10, 10, [], [], [], "Shark", 0)
        break
    elif classify == ("healer"):
        naming = input("What is your name? ")
        character = Bunny(naming, 200, 10, 0, [], [], [], "Bunny", 0)
        break
    elif classify == ("support"):
        naming = input("What is your name? ")
        character = Frog(naming, 200, 10, 0, [], [], [], "Frog", 0)
        break
    elif classify == ("poison"):
        naming = input("What is your name? ")
        character = Snake(naming, 200, 15, 0, [], [], [], "Snake", 0)
        break
    elif classify == ("sniper"):
        naming = input("What is your name? ")
        character = Falcon(naming, 175, 25, 0, [], [], [], "Falcon", 0)
        break
    elif classify == ("hypnotist"):
        naming = input("What is your name? ")
        character = Cat(naming, 200, random.randint(5, 25), 0, [], [], [], "Cat", 0)
        break
    else:
        print("Class not found. Maybe you misspelled the class name?")

print(character.__dict__)
time.sleep(2)

#Tutorial begins

print("Game starting...")
time.sleep(2)


print(f"Alright, you have chosen class {character.classed}.")
time.sleep(2)
print("Now, let's test your skills by fighting a goblin!")
print("")
time.sleep(1)

tutorialgoblin = TutorialGoblin("Goblin", 200, 250)

def tutorialbattle():
    print(f"{character.name} is now fighting {tutorialgoblin.name}!")
    time.sleep(2)
    abilityuse = 0

    while character.health > 0 and tutorialgoblin.health > 0:
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
            print(f"{character.name} did {character.damage} damage to {tutorialgoblin.name}!")
            tutorialgoblin.health = tutorialgoblin.health - character.damage
            time.sleep(2)
            if tutorialgoblin.health <= 0:
                tutorialgoblin.health = 0
            print(f"{tutorialgoblin.name} is now at {tutorialgoblin.health} health.")
            if tutorialgoblin.health <= 0:
                print(f"{tutorialgoblin.health} has been defeated!")
                messages = [
                    "Congratulations!",
                    "You have defeated your first goblin!",
                    "After winning a battle, you gain XP and a chest.",
                    "After every battle, win or loss, you can earn items, complete quests, and use the shop.",
                    "This way, you can grow more powerful and take on stronger enemies."
                ]
                for line in messages:
                    time.sleep(2)
                    print(line)
                    break

        elif action == 2:
            if not character.inventory:
                print("Inventory is still in the works and will come out in v2.0.")
                continue

        elif action == 3:
            if abilityuse >= 3:
                print("You have run out of ability usages this battle.")
                continue
            for i, ability in enumerate(character.abilities, start=1):
                print(f"{i}. {ability['abilityName']} (Damage: {ability['Damage']}, Heal: {ability['Heal']})")

            chooseability = int(input("Which ability would you like to use? ")) - 1
            chosen = character.abilities[chooseability]

            tutorialgoblin.health -= chosen["Damage"]
            character.health += chosen["Heal"]

            print(f"{character.name} used {chosen['abilityName']}!")
            abilityuse = abilityuse + 1
            time.sleep(2)
            print(f"{character.name} did {chosen['Damage']} damage to {tutorialgoblin.name}!")
            time.sleep(2)
            if tutorialgoblin.health <= 0:
                tutorialgoblin.health = 0
            print(f"{tutorialgoblin.name} is now at {tutorialgoblin.health} health.")
            time.sleep(2)
            print(f"{character.name} is now at {character.health} health.")
            time.sleep(1)
            if tutorialgoblin.health <= 0:
                print(f"{tutorialgoblin.name} has been defeated!")
                messages = [
                    "Congratulations!",
                    "You have defeated your first goblin!",
                    "After winning a battle, you gain XP and a chest.",
                    "After every battle, win or loss, you can earn items, complete quests, and use the shop.",
                    "This way, you can grow more powerful and take on stronger enemies."
                ]
                for line in messages:
                    time.sleep(2)
                    print(line)
                    break

        elif action == 4:
            print(f"{character.name} ran away!")
            return
        
        else: 
            print("This is not an action.")
            continue
        
        time.sleep(2)
        print(" ")
        print(f"{tutorialgoblin.name} is now attacking!")
        time.sleep(2)
        print(f"{tutorialgoblin.name} did {tutorialgoblin.damage} damage to {character.name}!")
        character.health = character.health - tutorialgoblin.damage
        time.sleep(2)
        print(f"{character.name} is now at {character.health} health.")
        print(" ")
        time.sleep(2)
        if character.health <= 0:
            print(f"{character.name} has been defeated!")
            return

tutorialbattle()

goblin = Enemy("Goblin", 200, 25)

def battle():
    print(f"{character.name} is now fighting {goblin.name}!")
    time.sleep(2)
    abilityuse = 0

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
                break

        elif action == 2:
            if not character.inventory:
                print("Inventory is still in the works and will come out in v2.0.")
                continue

        elif action == 3:
            if abilityuse >= 3:
                print("You have run out of ability usages this battle.")
                continue
            for i, ability in enumerate(character.abilities, start=1):
                print(f"{i}. {ability['abilityName']} (Damage: {ability['Damage']}, Heal: {ability['Heal']})")

            chooseability = int(input("Which ability would you like to use? ")) - 1
            chosen = character.abilities[chooseability]

            goblin.health -= chosen["Damage"]
            character.health += chosen["Heal"]

            print(f"{character.name} used {chosen['abilityName']}!")
            abilityuse = abilityuse + 1
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
        
#battle()
print("You have gained 10 XP!")
time.sleep(1)
print("You have recieved a chest!")

def commonchest():
    goldgain = random.randint(30,80)
    itemsgot = []

    loottable = {
    "Common": ['e'],
    "Rare": ['r'],
    "Epic": ['t'],
    "Legendary": ['y'],
    "Mythic": ['u'] 
    }

    raritypercent = {
        "Common": 51,
        "Rare": 30,
        "Epic": 14,
        "Legendary": 4,
        "Mythic": 1
    }

    itemcount = random.randint(1, 3)

    for i in range(itemcount):
        rarity = random.choices(
            list(raritypercent.keys()),
            weights = raritypercent.values(),
            k=1
        )[0]

        itemgot = random.choice(loottable[rarity])

        if rarity == ("Epic"):
            print(f"You have found an Epic {itemgot}!")
        else:
            print(f"You have found a {rarity} {itemgot}!")

        itemsgot.append(itemgot)
        character.inventory.append(itemgot)

    character.gold += goldgain
    return itemgot, goldgain
commonchest()
print(character.inventory)
print(character.gold)