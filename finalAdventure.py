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
    def __init__(self, name, health, damage, shield, abilities, inventory):
        abilities = [
            {"abilityName":"Cat Meow","dmg":0,"heal":25,},
            {"abilityName":"Cat Claws","dmg":50,"heal":0,},
            {"abilityName":"Cat Eyes","dmg":random(0,67),"heal":0,},
            {"abilityName":"Angry Cat Attack","dmg":75,"heal":0,}
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
            {"abilityName":"Falcon Dive","dmg":75,"heal":0,},
            {"abilityName":"Falcon Feathers","dmg":20,"heal":0,},
            {"abilityName":"Falcon Screech","dmg":50,"heal":0,},
            {"abilityName":"Falcon Claw","dmg":40,"heal":0,},
            {"abilityName":"Falcon Beak","dmg":40,"heal":0,}
            
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
            {"abilityName":"Snake Venom","dmg":33,"heal":0,},
            {"abilityName":"Snake Crush","dmg":40,"heal":0,},
            {"abilityName":"Snake Fangs","dmg":40,"heal":0,},
            {"abilityName":"Snake Hiss","dmg":20,"heal":10,}

            
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
            {"abilityName":"Frog Boost","dmg":33,"heal":0,},
            {"abilityName":"Frog Assist","dmg":20,"heal":30},
            {"abilityName":"Frog Vial","dmg":10,"heal":random(50,67),}
           
            
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
            {"abilityName":"Shark Attack","dmg":50,"heal":0,},
            {"abilityName":"Shark Fin","dmg":45,"heal":30},
            {"abilityName":"Shark Tail Swing","dmg":25,"heal":25,},
            {"abilityName":"Shark Skin","dmg":33,"heal":0,},
            {"abilityName":"Shark Teeth","dmg":67,"heal":1}
           
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
            {"abilityName":"Bunny Heal","dmg":0,"heal":50,},
            {"abilityName":"Bunny Shield","dmg":25,"heal":30},
            {"abilityName":"Bunny Protection","dmg":30,"heal":25,}
            
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
            {"abilityName":"Penguin Slap","dmg":44,"heal":0,},
            {"abilityName":"Penguin Punch","dmg":65,"heal":0,},
            {"abilityName":"Penguin Slide","dmg":5,"heal":50,},
            {"abilityName":"Penguin Beak Attack","dmg":35,"heal":0,},
            {"abilityName":"Penguin Stomp","dmg":random(25,50),"heal":1,}

            
        ]
        self.name = name
        self.health = health
        self.damage = damage
        self.shield = shield
        self.abilities = abilities
        self.inventory = inventory
