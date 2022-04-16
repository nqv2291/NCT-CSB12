from asyncio import shield
from unicodedata import name


storage = {
    "HP":20,
    "DELL":50,
    "MACBOOK":12,
    "ASUS":30
}

price = {
    "HP":600,
    "DELL":650,
    "MACBOOK":1200,
    "ASUS":400
}

player={
    "Name":"yuri4life",
    "Age": 17,
    "Lv":2,
    "Gold":100,
    "HP":100,
    "DEF":10,
    "ATK":8,
    "Backpack":['shield','bread loaf']
}

skill_set=[
    {"Name":"Tackle", "Minimum level": 1, "Damage": 5, "Hit rate": 0.3},
    {"Name": "Quick Attack","Minimum level": 2, "Damage": 3, "Hit rate": 0.5},
    {"Name": "Strong Kick", "Minimum level": 4, "Damage": 9, "Hit rate": 0.2}
]