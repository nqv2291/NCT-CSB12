player = [ 
    {
		'Name': 'Tackle', 
        'Minimum level': 1, 
        'Damage': 5,
        'Hit rate': 0.3,
	},
	{
        'Name': 'Quick Attack',
        'Minimum level': 2, 
        'Damage': 3, 
        'Hit rate': 0.5,
	},
	{
        'Name': 'Strong Kick',
        'Minimum level': 4,
        'Damage': 9,
        'Hit rate': 0.2
	}
]   

for i in range(3):
    print(f"Skill {i+1}: {player[i]['Name']}")

chose = int(input("Choose skill by number: "))
print("You chose", player[chose - 1]['Name'])
LevelMin = player[chose - 1]['Minimum level']
LevelMax = 4

if LevelMin >= LevelMax:
    print("Cannot deploy. Required level 4.")
else:
    print("Damage:", player[chose - 1]['Damage'] )
