#Setup map
map = [
    ["-","-","-","-"],
    ["-","-","-","-"],
    ["-","-","-","-"],
    ["-","-","-","-"]
]
#Vị trí của người chơi, cửa và chìa khóa: là tọa độ với trục Ox hướng sang ngang(trái sang phải) và Oy hướng xuống dưới (trên xuống dưới)
player_x = 1
player_y = 1

door_x = 3
door_y = 2

key_x = 4
key_y = 3
key_picked = False
#Hàm này dùng để refresh map sau mỗi lần di chuyển, hơi phức tạp do phải tiếp cận index của list trong list
def init_map():
    map[player_y-1][player_x-1] = "P"
    map[door_y-1][door_x-1] = "D"
    if key_picked == False:    
        map[key_y-1][key_x-1] = "K"
    else:
        map[key_y-1][key_x-1] = "❤"  
    for i in map:
        print(i,end="\n")

#Hàm này dùng để loại bỏ vị trí cũ của player mỗi khi di chuyển hoặc xóa key      
def remove_object(x,y):
    map[y-1][x-1] = "-"

def pickup_key():
    remove_object(key_x,key_y)
    global key_picked
    key_picked = True
while True:
    init_map()
    move = input("What's your next move? WASD or Q to quit: ")
    if move.upper() == "W":
        remove_object(player_x,player_y)
        player_y-=1 #khi W thì tung độ của player sẽ bị giảm đi 1
    elif move.upper() == "S":
        remove_object(player_x,player_y)
        player_y+=1 #khi S thì tung độ của player sẽ bị tang lên 1   
    elif move.upper() == "A":
        remove_object(player_x,player_y)
        player_x-=1 #khi A thì hoành độ của player sẽ bị giảm đi 1      
    elif move.upper() == "D":
        remove_object(player_x,player_y)
        player_x+=1 #khi D thì hoành độ của player sẽ bị tăng lên 1   
    elif move.upper() == "Q":  
        print('You quitted')  
        break
    else:
        print("Invalid, try again")
    

    if key_x==player_x and key_y==player_y:
        print("===YOU HAVE THE KEY, NOW GO TO THE DOOR===")
        pickup_key()

    if player_x==door_x and player_y==door_y and key_picked == True:
        print("===YOU WIN!!!===")  
        break
    elif player_x==door_x and player_y==door_y and key_picked == False:
        print("===YOU NEED THE KEY TO GET OUT===")  