import random

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
        'Hit rate': 0.1,
	},
	{
        'Name': 'Strong Kick',
        'Minimum level': 4,
        'Damage': 9,
        'Hit rate': 0.2
	}
]   
#intro
for i in range(3):
    print(f"Skill {i+1}: {player[i]['Name']}")

#body
chose = int(input("Choose skill by number: "))
print("You chose", player[chose - 1]['Name'])

#check
LevelMin = player[chose - 1]['Minimum level']
LevelMax = 4
hitMin = random.random()
hitMax = player[chose - 1]['Hit rate']
#end
if LevelMin >= LevelMax and hitMin >= hitMax:
    print("Missed")
else:
    print("Damage:", player[chose - 1]['Damage'] )