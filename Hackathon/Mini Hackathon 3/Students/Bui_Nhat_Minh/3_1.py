import os
import math
import msvcrt
import random


def get_random_number(min, max):
    return random.randint(min, max)


def create_map():
    os.system('cls')
    print('== THE ESCAPE GAME ==')
    print('Use W A S D to move the (P)layer.')
    print('Find (K)ey first then exit through the (D)oor.')


def print_map(width, height, player_x, player_y, key_x, key_y, door_x, door_y):
    if (turn > 0):
        os.system('cls')
    for y in range(height):
        for x in range(width):
            if x == player_x and y == player_y:
                print('P', end='')
            elif x == key_x and y == key_y:
                print('K', end='')
            elif x == door_x and y == door_y:
                print('D', end='')
            else:
                print('-', end='')
        print()


# Game initialization
create_map()

turn = 0
key_collected = False
door_reach = True

room_width, room_height = random.randint(5, 10), random.randint(5, 10)
player_pos_x = random.randint(0, room_width - 1)
player_pos_y = random.randint(0, room_height - 1)
key_pos_x = random.randint(0, room_width - 1)
key_pos_y = random.randint(0, room_height - 1)
while key_pos_x == player_pos_x and key_pos_y == player_pos_y:
    key_pos_x = random.randint(0, room_width - 1)
    key_pos_y = random.randint(0, room_height - 1)
door_pos_x = random.randint(0, room_width - 1)
door_pos_y = random.randint(0, room_height - 1)
while key_pos_x == door_pos_x and key_pos_y == door_pos_y:
    door_pos_x = random.randint(0, room_width - 1)
    door_pos_y = random.randint(0, room_height - 1)
print_map(room_width, room_height, player_pos_x, player_pos_y,
          key_pos_x, key_pos_y, door_pos_x, door_pos_y)

# Gameplay


def check_move(move):
    global player_pos_x, player_pos_y, key_pos_x, key_pos_y, door_pos_x, door_pos_y, room_height, room_width
    if move == 'w' and player_pos_y > 0:
        player_pos_y -= 1
    elif move == 's' and player_pos_y < room_height - 1:
        player_pos_y += 1
    elif move == 'a' and player_pos_x > 0:
        player_pos_x -= 1
    elif move == 'd' and player_pos_x < room_width - 1:
        player_pos_x += 1


def check_win_condition():
    global key_collected
    global door_reach

    os.system('cls')
    door_reach = True
    if (key_collected):
        print('You win!')
        print(f'You completed the game in {turn} turns.')
    else:
        print('You lose!')
        print('Please remember to collect the key before exiting the door.')


while True:
    move = msvcrt.getch().decode('utf-8')
    if move == 'w' or move == 's' or move == 'a' or move == 'd':
        check_move(move)
        turn += 1
        if key_pos_x == player_pos_x and key_pos_y == player_pos_y:
            key_collected = True
            key_pos_x = -1
            key_pos_y = -1
        if door_pos_x == player_pos_x and door_pos_y == player_pos_y:
            check_win_condition()
            break

        print_map(room_width, room_height, player_pos_x, player_pos_y,
                  key_pos_x, key_pos_y, door_pos_x, door_pos_y)
    elif move == 'q':
        break
