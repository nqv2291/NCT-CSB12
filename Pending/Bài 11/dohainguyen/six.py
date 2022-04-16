from dict import player
wick=[]
player['Gold']=player['Gold']+50
print("Gold:",player['Gold'])

player["Backpack"].append("Flint")

print("Backpack:",end=" ")
for i in range(len(player["Backpack"])):
    print (player["Backpack"][i],end=",")