#Penguin is damage
class Penguin():
    def __init__(self, name, health, damage, shield, ability, inventory):
        ability = [
            {"name":"Penguin Slap", "damage":25,},
            {"name":"Penguin Punch", "damage":40,},
            {"name":"Penguin Strike", "damage":50,},
            {"name":"Penguin Beak Attack", "damage":67,},
            {"name":"Penguin Stomp", "damage":50,},
        ]
        self.name = name
        self.health = health
        self.damage = damage
        self.shield = shield
        self.ability = ability[2]
        self.inventory = inventory

luke = Penguin("Luke", 100, 50, 0, "", [""])
print(luke.__dict__)