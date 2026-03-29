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