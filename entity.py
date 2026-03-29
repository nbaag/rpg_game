from stats import Stats
from data import RACE_BONUSES

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