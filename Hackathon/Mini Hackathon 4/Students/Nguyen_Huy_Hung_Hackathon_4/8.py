import random as r
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

character = {
    'Name': 'Light',
    'Age': 17,
    'Strength': 8,
    'Defense': 10,
    'HP': 100,
    'Backpack': ['Shield', 'Bread Loaf'],
    'Gold': 100,
    'Level': 2
}

for i in range(len(skills)):
    print(f'''Skill {i+1}: {skills[i]['Name']}''')
inp = int(input('Choose skill by number: \n'))
print(f'''You chose {skills[inp-1]["Name"]}''')

if character["Level"] >= skills[inp-1]["Minimum Level"]:
    print(f"""Damage: {skills[inp-1]["Damage"]}""")
else:
    print(f"""Cannot deploy. Required level {skills[inp-1]["Minimum Level"]}""")

rate = r.random()
for i in range(len(skills)):
    print(f'''Skill {i+1}: {skills[i]['Name']}''')
inp = int(input('Choose skill by number: '))
print(f'''You chose {skills[inp-1]["Name"]}''')

if character["Level"] >= skills[inp-1]["Minimum Level"]:
    if rate <= skills[inp-1]["Hit Rate"]:
        print(f"""Damage: {skills[inp-1]["Damage"]}""")
    else:
        print("Missed")
else:
    print(f"""Cannot deploy. Required level {skills[inp-1]["Minimum Level"]}""")