from dataclasses import dataclass, field

from statModifier import StatModifier


@dataclass
class BaseStats:
    strength: int
    agility: int
    intelligence: int
    wisdom: int
    endurance: int


class Stats:
    base: BaseStats
    modifiers: list[StatModifier] = field(default_factory=list)

    def get(self, name: str) -> int:
        base = getattr(self.base, name)
        bonus = sum(m.value for m in self.modifiers if m.stat == name)
        return base + bonus

    @property
    def attack_power(self) -> int:
        return self.get("strength") * 2

    @property
    def max_hp(self) -> int:
        return self.get("endurance") * 2

    @property
    def max_mana(self) -> int:
        return self.get("wisdom") * 2

    @property
    def magic_power(self) -> int:
        return self.get("intelligence") * 2

    @property
    def dodge(self) -> int:
        return self.get("agility") * 2

    @property
    def defence(self) -> int:
        return self.get("endurance") * 2

        # make more stats?
