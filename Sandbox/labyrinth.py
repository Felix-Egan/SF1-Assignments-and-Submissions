# A labyrinth game where the walls move:

import random

def print_labyrinth(labyrinth):
    for row in labyrinth:
        print(''.join(row))

def move_player(labyrinth, player, direction):
    new_player = player[:]
    if direction == 'up':
        new_player[0] -= 1
    elif direction == 'down':
        new_player[0] += 1
    elif direction == 'left':
        new_player[1] -= 1
    elif direction == 'right':
        new_player[1] += 1
    if labyrinth[new_player[0]][new_player[1]] == ' ':
        labyrinth[player[0]][player[1]] = ' '
        labyrinth[new_player[0]][new_player[1]] = 'P'
        return new_player
    return player

def move_walls(labyrinth):
    for row in range(1, len(labyrinth) - 1):
        for col in range(1, len(labyrinth[row]) - 1):
            if labyrinth[row][col] == 'W':
                direction = random.choice(['up', 'down', 'left', 'right'])
                if direction == 'up':
                    if labyrinth[row - 1][col] == ' ':
                        labyrinth[row - 1][col] = 'W'
                        labyrinth[row][col] = ' '
                elif direction == 'down':
                    if labyrinth[row + 1][col] == ' ':
                        labyrinth[row + 1][col] = 'W'
                        labyrinth[row][col] = ' '
                elif direction == 'left':
                    if labyrinth[row][col - 1] == ' ':
                        labyrinth[row][col - 1] = 'W'
                        labyrinth[row][col] = ' '
                elif direction == 'right':
                    if labyrinth[row][col + 1] == ' ':
                        labyrinth[row][col + 1] = 'W'
                        labyrinth[row][col] = ' '

def main():
    labyrinth = [
        list(' WWW WWW '),
        list('W       W'),
        list('W WWWW  W'),
        list('W W   W W'),
        list('W W W W W'),
        list('W     W W'),
        list('WWWWWWWWW')
    ]
    player = [1, 1]
    labyrinth[player[0]][player[1]] = 'P'
    print_labyrinth(labyrinth)
    while True:
        direction = input('Enter direction: ')
        player = move_player(labyrinth, player, direction)
        move_walls(labyrinth)
        print_labyrinth(labyrinth)

main()