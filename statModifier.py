from dataclasses import dataclass


@dataclass
class StatModifier:
    name: str
    stat: str
    value: int
    source: str
    duration: int | None = None
