#Bai 1
lst ={
    'Name': 'Light',
    'Age': '17',
    'Strength': '8',
    'Defense': '10',
    'HP': '100',
    'Backpack': 'Shield,Bread Loaf',
    'Gold': '100',
    'Level': '2'
}
for key in lst.keys():
    print(key + ":" +lst[key])

#Bai 2
lst ={
    'Name': 'Light',
    'Age': '17',
    'Strength': '8',
    'Defense': '10',
    'HP': '100',
    'Backpack': 'Shield,Bread Loaf',
    'Gold': '100',
    'Level': '2'
}
lst['Gold'] = '150'
for key in lst.keys():
    print(key + ":" +lst[key])

#Bai 3
lst ={
    'Name': 'Light',
    'Age': '17',
    'Strength': '8',
    'Defense': '10',
    'HP': '100',
    'Backpack': 'Shield,Bread Loaf',
    'Gold': '100',
    'Level': '2'
}
lst['Backpack'] = 'Shield,Bread \n Loaf,FlinStone'
for key in lst.keys():
    print(key + ":" +lst[key])