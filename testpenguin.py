#Penguin is damage
class Penguin():
    def __init__(self, name, health, damage, shield, ability, inventory):
        ability = [
            {"Name": "Penguin Slap"},
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