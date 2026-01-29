from dataclasses import dataclass

from stats import Stats


@dataclass
class Entity:
    name: str
    level: int
    entity_class: str
    stats: Stats
    hp: int
    mana: int
