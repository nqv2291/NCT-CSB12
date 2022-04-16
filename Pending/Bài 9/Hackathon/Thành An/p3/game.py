import random

def drawMap():
    map = []
    for i in range(random.randint(5, 10)):
        map.append(["-"] * random.randint(5, 10))
    player = [random.randint(0, len(map) - 1), random.randint(0, len(map[0]) - 1)]
    key = [random.randint(0, len(map) - 1), random.randint(0, len(map[0]) - 1)]
    door = [random.randint(0, len(map) - 1), random.randint(0, len(map[0]) - 1)]
    map[player[0]][player[1]] = "P"
    map[key[0]][key[1]] = "K"
    map[door[0]][door[1]] = "D"
    return map

for row in drawMap():
    print(row)


    
    


    


    

    






