#combat function, player creation, starter zone - race

import time
import sys

class Entity:
    BASE_STATS = {
        "Strength": 0,
        "Dexterity": 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Endurance": 0,
    }

    def __init__(self, name, race, level, profession=None):
        self.name = name
        self.race = race
        self.level = level
        self.stats = self.BASE_STATS.copy()
        self.health = 0
        self.mana = 0
        self.profession = profession
        

class Profession:
    def __init__(self, title, damage_stat, abilities=None, allowed_weapons=None, allowed_armor=None):
        self.title = title
        self.damage_stat = damage_stat 
        self.abilities = abilities or []
        self.allowed_weapons = allowed_weapons or []
        self.allowed_armor = allowed_armor or []

    def __repr__(self):
        return f"Profession({self.title})"
    

class Ability:
    def __init__(self, name, required_level, damage_stat, power, cooldown):
        self.name = name
        self.required_level = required_level
        self.damage_stat = damage_stat
        self.power = power
        self.cooldown = cooldown

    def __repr__(self):
        return f"Ability({self.name}, lv {self.required_level})"

        

def typing_effect(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


warrior = Profession(
    title="Warrior",
    damage_stat="Strength",
    abilities=[
        Ability(
            name="Slash", 
            required_level=1, 
            damage_stat="Strength", 
            power=10, 
            cooldown=0
        ),
        Ability(
            name="Block", 
            required_level=2, 
            damage_stat="Endurance", 
            power=10, 
            cooldown=2
        )
    ]
)

mage = Profession(
    title="Mage",
    damage_stat="Intelligence",
    abilities=[
        Ability(
            name="Frostbolt", 
            required_level=1, 
            damage_stat="Intelligence", 
            power=10, 
            cooldown=0
        ),
        Ability(
            name="Fireblast", 
            required_level=3, 
            damage_stat="Intelligence", 
            power=20, 
            cooldown=2
        )
    ]
)

rogue = Profession(
    title="Rogue",
    damage_stat="Dexterity",
    abilities=[
        Ability(
            name="Backstab",
            required_level=1,
            damage_stat="Dexterity",
            power=10,
            cooldown=0
        ),
        Ability(
            name="Evasion",
            required_level=3,
            damage_stat="Dexterity",
            power=20,
            cooldown=2
        )
    ]
)

priest = Profession(
    title="Priest",
    damage_stat="Wisdom",
    abilities=[
        Ability(
            name="Holylight",
            required_level=1,
            damage_stat="Wisdom",
            power=10,
            cooldown=1
        ),
        Ability(
            name="Banisment",
            required_level=3,
            damage_stat="Wisdom",
            power=30,
            cooldown=3
        )
    ]
)

races = {
    "1": "Human",
    "2": "Elf",
    "3": "Dwarf"
}


classes = {
    "1": warrior,
    "2": mage,
    "3": rogue,
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
    