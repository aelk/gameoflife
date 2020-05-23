import os
import time
from random import randint

def dead_state(width, height):
    return [[0 for i in range(width)] for j in range(height)]

def random_state(width, height):
    state = dead_state(width, height)
    for i in range(height):
        for j in range(width):
            state[i][j] = randint(0, 1)
    return state

def render(state):
    border_width = len(state[0]) + 2;
    print("-" * border_width)
    for row in state:
        print('|', end='')
        for cell in row:
            print(' ' if cell == 0 else '#', end='')
        print('|')
    print("-" * border_width)

def count_live_neighbors(state, pos):
    x, y = pos
    live_neighbors = 0

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i < 0 or j < 0 or i >= len(state) or j >= len(state[0]):
                continue
            elif state[i][j] == 1 and (i, j) != pos:
                live_neighbors += 1

    return live_neighbors

def update_cell(cell, neighbors):
    return (cell == 0 and neighbors == 3) or \
            (cell == 1 and (neighbors < 2 or neighbors > 3))

def next_board_state(state):
    positions_to_update = []
    for i in range(len(state)):
        for j in range(len(state[0])):
            cell = state[i][j]
            pos = (i, j)
            live_neighbors = count_live_neighbors(state, pos)
            if update_cell(cell, live_neighbors):
                positions_to_update.append(pos)

    for pos in positions_to_update:
        x, y = pos
        state[x][y] ^= 1

    return state

if __name__ == '__main__':
    width, height = 63, 70
    state = random_state(width, height)
    for i in range(3000):
        os.system('clear')
        render(state)
        print("Generation", i)
        time.sleep(0.3)
        state = next_board_state(state)
