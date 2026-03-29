#combat function, player creation, starter zone - race
# Разобраться со скейлингом
# Продумать как будут скейлится другие спелы

import time
import sys
from dataclasses import dataclass, field

class Stats:
    BASE = {
        "Strength": 1,
        "Dexterity": 1,
        "Intelligence": 1,
        "Wisdom": 1,
        "Endurance": 1,
    }

    def __init__(self):
        self.base = self.BASE.copy()
        self.bonuses = {}

    def add_bonus(self, source, values):
        self.bonuses[source] = values

    def remove_bonus(self, source):
        self.bonuses.pop(source, None)

    def get(self, stat):
        total = self.base.get(stat, 0)
        for bonus in self.bonuses.values():
            total += bonus.get(stat, 0)
        return total
    
    def get_attack_power(self):
        return self.get("Strength") * 2
    
    def get_crit_chance(self):
        return self.get("Dexterity") * 0.5
    
    def get_evasion(self):
        return self.get("Dexterity") * 0.3
    
    def get_spell_power(self):
        return self.get("Intelligence") * 3
    
    def get_spell_crit(self):
        return self.get("Intelligence") * 0.3
    
    def get_health(self):
        return self.get("Endurance") * 5
    
    def get_mana(self):
        return self.get("Wisdom") * 5
    
    def __repr__(self):
        stats = {stat: self.get(stat) for stat in self.base}
        return f"Stats({stats})"
    
@dataclass
class Ability:
    name: str
    required_level: int
    damage_stat: str
    power: int
    cooldown: float
    scaling: float

    def calculate_damage(self, caster):
        if self.damage_stat == "Strength":
            return self.power + caster.stats.get_attack_power() * self.scaling
        elif self.damage_stat == "Intelligence":
            return self.power + caster.stats.get_spell_power() * self.scaling
        else:
            return self.power + caster.stats.get(self.damage_stat) * self.scaling


@dataclass
class Profession:
    title: str
    energy_name: str
    energy_max: int | None
    energy_starts_full: bool = False
    abilities: list = field(default_factory=list)
    allowed_weapons: list = field(default_factory=list)
    allowed_armor: list = field(default_factory=list)
    

class Entity:
    def __init__(self, name, race, level, profession=None):
        self.name = name
        self.race = race
        self.level = level
        self.profession = profession
        self.stats = Stats()
        self.stats.add_bonus("race", RACE_BONUSES.get(race, {}))
        self.health = self.stats.get_health()
        self.energy_max = self._calculate_energy()
        self.energy = self.energy_max if self.profession.energy_starts_full else 0

    def _calculate_energy(self):
        if self.profession.energy_max is None:
            return self.stats.get_mana()
        return self.profession.energy_max

RACES = {
    "1": "Human",
    "2": "Elf",
    "3": "Dwarf"
}

RACE_BONUSES = {
    "Human": {"Strength": 1, "Dexterity": 1, "Intelligence": 1, "Wisdom": 1, "Endurance": 1},
    "Elf": {"Strength": 0, "Dexterity": 2, "Intelligence": 2, "Wisdom": 1, "Endurance": 0},
    "Dwarf": {"Strength": 2, "Dexterity": 0, "Intelligence": 0, "Wisdom": 1, "Endurance": 2}
}
        

def typing_effect(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


warrior = Profession(
    title="Warrior",
    energy_name="Rage",
    energy_max=100,
    energy_starts_full=False,
    abilities=[
        Ability(
            name="Slash", 
            required_level=1, 
            damage_stat="Strength", 
            power=10, 
            cooldown=0,
            scaling=1.0
        ),
        Ability(
            name="Block", 
            required_level=2, 
            damage_stat="Endurance", 
            power=10, 
            cooldown=2,
            scaling=1.0
        )
    ]
)

mage = Profession(
    title="Mage",
    energy_name="Mana",
    energy_max=None,
    energy_starts_full=True,
    abilities=[
        Ability(
            name="Frostbolt", 
            required_level=1, 
            damage_stat="Intelligence", 
            power=10, 
            cooldown=0,
            scaling=1.0
        ),
        Ability(
            name="Fireblast", 
            required_level=3, 
            damage_stat="Intelligence", 
            power=20, 
            cooldown=2,
            scaling=1.0
        )
    ]
)

rogue = Profession(
    title="Rogue",
    energy_name="Focus",
    energy_max=100,
    energy_starts_full=True,
    abilities=[
        Ability(
            name="Backstab",
            required_level=1,
            damage_stat="Dexterity",
            power=10,
            cooldown=0,
            scaling=1.0
        ),
        Ability(
            name="Evasion",
            required_level=3,
            damage_stat="Dexterity",
            power=20,
            cooldown=2,
            scaling=1.0
        )
    ]
)

priest = Profession(
    title="Priest",
    energy_name="Mana",
    energy_max=None,
    energy_starts_full=True,
    abilities=[
        Ability(
            name="Holylight",
            required_level=1,
            damage_stat="Wisdom",
            power=10,
            cooldown=1,
            scaling=1.0
        ),
        Ability(
            name="Banishment",
            required_level=3,
            damage_stat="Wisdom",
            power=30,
            cooldown=3,
            scaling=1.0
        )
    ]
)


CLASSES = {
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

    