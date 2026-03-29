from dataclasses import dataclass, field

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