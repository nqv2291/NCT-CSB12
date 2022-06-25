import collections


character = {
    "Name" : "Light",
    "Age" : 17,
    "Strength" : 8,
    "Def" : 10,
    "Hp" : 100,
    "Backpack" : ["Shield , Bread"],
    "Gold" : 100,
    "Level" : 2
}

character["Gold"] = character["Gold"] + 50
print(f"gold: {character['Gold']}")
character["Backpack"] = "Shield , Bread, flintstone,"
