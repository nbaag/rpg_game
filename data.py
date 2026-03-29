from profession import warrior, mage, rogue, priest

CLASSES = {
    "1": warrior,
    "2": mage,
    "3": rogue,
    "4": priest
}

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