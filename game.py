#combat function, player creation, starter zone - race

import time
import sys

class Entity:
    def __init__(self, name, race, level, profession=None):
        self.name = name
        self.race = race
        self.level = level
        self.stats = base_stats.copy()
        self.health = 0
        self.mana = 0
        self.profession = profession
        

class Profession:
    def __init__(self, title, damage_stat):
        self.title = title
        self.damage_stat = damage_stat 
        self.abilities = []
        self.allowed_weapons = []
        self.allowed_armor = []
        

def typing_effect(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def combat_start(player, enemies):
    if isinstance(enemies, str):
        enemies = [enemies]
    print(f"{player.name} in fight with {', '.join(enemies)}")


def attack(attacker, target):
    target.health -= attacker.attack
    print(f"{attacker} hits {target} for {attacker.attack}")


base_stats = {
    "Strength": 0,
    "Dexterity": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Endurance": 0,
}


warrior = Profession("Warrior", "Strength")
warrior.abilities = ["Slash", "Block"]

mage = Profession("Mage", "Intelligence")
mage.abilities = ["Fireball", "Ice Spike"]

thief = Profession("Thief", "Dexterity")
thief.abilities = ["Backstab", "Evasion"]

priest = Profession("Priest", "Wisdom")
priest.abilities = ["Holylight", "Banishment"]

races = {
    "1": "Human",
    "2": "Elf",
    "3": "Dwarf"
}


classes = {
    "1": warrior,
    "2": mage,
    "3": thief,
    "4": priest
}


#Character creation
# typing_effect("Old sage: Look at you!\n")
# typing_effect("Old sage: What village are you from?\n")
# typing_effect("Choose your race (1 - Human, 2 - Elf, 3 - Dwarf)\n")


# while True:
#     player_race = input()

#     if player_race in races:
#         typing_effect("Old sage: Yeah, I can tell\n")
#         break        
#     else:
#         print("No, you are not!")


# typing_effect("Old sage: And what's your name?\n")
# player_name = input("Enter your name: ")
# typing_effect("Old sage: Right. Take a sit. And tell me your story.\n")

# player = Entity(player_name, races[player_race], 10, 10, 1)

# print(player.name, player.race, player.level)

#test
player_name = input("Enter your name: ")
player_race = input("Enter your race: ")
player_profession = input("Choose class: 1 - Warrior, 2 - Mage, 3 - Thief, 4 - Priest")

player = Entity(player_name, player_race, 1)
player.profession = classes[player_profession]

print(f"You are {player.race} - {player.name}, your profession is {player.profession.title} Lv {player.level}. You have {player.profession.abilities}")
    