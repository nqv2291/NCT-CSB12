import random as r

# Map size
HEIGHT = 10
WIDTH = 10


## functions---------------------------------------------------------------------
# initialize map
def init_map():
    # create an empty map size HEIGHT x WIDTH
    # get object position = game_map[row][col]
    global game_map
    game_map = [ ["-" for col in range(WIDTH)] for row in range(HEIGHT) ]#list comprehension

    # choose random position for P, D, K
    global obj, obj_pos
    obj = ["P", "D", "K"]
    obj_pos = []

    for i in range(len(obj)):
        # execute a while loop until P, D, K get different positions
        while len(obj_pos) != (i + 1):
            # get random column and row
            r_row = r.randint(0, HEIGHT - 1)
            r_col = r.randint(0, WIDTH - 1)

            # store object position: [row, col]
            temp_pos = [r_row, r_col]
            if temp_pos not in obj_pos: # only add new position
                obj_pos.append(temp_pos)
                game_map[r_row][r_col] = obj[i]


# print map
def print_map():
    for row in game_map:
        print(" ".join(row))


# find player direction
def player_dir(key):
    p_new_pos = p_cur_pos.copy() # p_new_pos = [row, col]

    if key == "a":
        print("Go left")
        p_new_pos[1] = p_new_pos[1] - 1
        player_move(p_new_pos)
    elif key == "d":
        print("Go right")
        p_new_pos[1] = p_new_pos[1] + 1
        player_move(p_new_pos)
    elif key == "w":
        print("Go up")
        p_new_pos[0] = p_new_pos[0] - 1
        player_move(p_new_pos)
    elif key == "s":
        print("Go down")
        p_new_pos[0] = p_new_pos[0] + 1
        player_move(p_new_pos)
    else:
        print("Invalid command. Please try again")

# change player position
def player_move(p_new_pos):
    global p_cur_pos

    if p_new_pos == door_pos:
        if game_map[key_pos[0]][key_pos[1]] == "K":
            print("You need to find the key first")
        else:
            global game_play
            game_play = False
            print("\n*** Congratulations. You won the game! ***")
    else: 
        game_map[p_new_pos[0]][p_new_pos[1]] = "P"
        game_map[p_cur_pos[0]][p_cur_pos[1]] = "-"        
        p_cur_pos = p_new_pos
        if p_new_pos == key_pos:
            print("Tadaa you've got the key")

## main program------------------------------------------------------------------
init_map()
game_play = True

p_cur_pos = obj_pos[0]
door_pos  = obj_pos[1]
key_pos   = obj_pos[2]

while game_play:
    print()
    print_map()

    # get user input
    print("\nEnter A, S, D, W to move around or Q to quit")
    user_input = input("=> Your choice: ")

    if user_input == "q":
        print("\nSee you later. Bye")
        break
    else:
        player_dir(user_input)