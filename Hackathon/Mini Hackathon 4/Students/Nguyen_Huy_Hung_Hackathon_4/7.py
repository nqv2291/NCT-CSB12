skills = [
    {
        "Name": "Tackle",
        "Minimum Level": 1,
        "Damage": 5,
        "Hit Rate": 0.3
    },
    {
        "Name": "Quick Attack",
        "Minimum Level": 2,
        "Damage": 3,
        "Hit Rate": 0.5
    },
    {
        "Name": "Strong Kick",
        "Minimum Level": 4,
        "Damage": 9,
        "Hit Rate": 0.2
    }
]

for i in range(len(skills)):
    print(f'''Skill {i+1}: {skills[i]['Name']}''')