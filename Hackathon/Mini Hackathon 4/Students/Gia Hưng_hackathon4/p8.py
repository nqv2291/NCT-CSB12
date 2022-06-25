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

char_skills = [
    {
        "skill" : "skill 1",
        "Name" : "Tackle",
        "Min_level" : 1,
        "Damage" : 3,
        "Hit_rate" : 0.3
    },
    {
        "skill" : "skill 2",
        "Name" : "Quick attack",
        "Min_level" : 2,
        "Damage" : 3,
        "Hit_rate" : 0.5
    },
    {
        "skill" : "skill 3",
        "Name" : "Strong kick",
        "Min_level" : 4,
        "Damage" : 9,
        "Hit_rate" : 0.2
    }
]

for i in range(len(char_skills)):
    print(f"{char_skills[i]['skill']}: {char_skills[i]['Name']}")

choose_skill = abs(int(input("Choose skill by number")))
if choose_skill > 3:
    print("you don't have enough skills")
skill_pos = choose_skill - 1
print(f"you chose {char_skills[skill_pos]['Name']}")
if( char_skills[skill_pos]["Min_level"] > character["Level"]):
    print(f"cannot deploy, required level {char_skills[skill_pos]['Min_level']}")
else:
    print(f"damage: {char_skills[skill_pos]['Damage']}")