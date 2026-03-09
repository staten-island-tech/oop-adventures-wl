import random

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
    return itemgot, goldgain
chest()