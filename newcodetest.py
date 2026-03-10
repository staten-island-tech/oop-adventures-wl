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
        
def chest():
    goldgain = random.randint(30,80)

    commonitem = ["e"]
    rareitem = ["r"]
    epicitem = ["t"]
    legendaryitem = ["y"]
    mythicitem = ["u"]

    decider = random.randint(1,100)

    if decider < 51:
        itemgot = commonitem
        rarity = "Common"
    elif decider < 75:
        itemgot = rareitem
        rarity = "Rare"
    elif decider < 89:
        itemgot = epicitem
        rarity = "Epic"
    elif decider < 97:
        itemgot = legendaryitem
        rarity = "Legendary"
    else:
        itemgot = mythicitem
        rarity = "Mythic"

    print(f"You have recieved {goldgain} gold and found a {rarity} {itemgot}!")
    int(character.gold) == int(character.gold) + int(goldgain)
    itemgot.append(character.inventory)
    return itemgot, goldgain
chest()
print(character.inventory)
print(character.gold)