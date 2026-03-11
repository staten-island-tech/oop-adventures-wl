import random

class Character:
    def __init__(self, name, health, damage, shield, inventory, equipinven, equippables, classed, gold):
        self.name = name
        self.health = health
        self.damage = damage
        self.shield = shield
        self.inventory = inventory
        self.abilities = []
        self.enquipinven = equipinven
        self.equippables = equippables
        self.classed = classed
        self.gold = gold
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

while True:
    classify = input("What class would you like to be? Damage, Tank, Healer, Support, Poison, Sniper, Hypnotist. ").lower()
    if classify == ("damage"):
        naming = input("What is your name? ")
        character = Penguin(naming, 175, 30, 0, [], [], [], "Penguin", 0)
        break
        
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

    itemcount = random.randint(5, 7)

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