


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