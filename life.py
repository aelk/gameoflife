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

def next_board_state(state):
    # count_live_neighbors(state, pos) -> returns 0..8

    # when a cell changes, append its pos to a list
    # after you finish checking each cell, go through the list
    # and toggle each of the positions
    new_cell_positions = []

    return state

if __name__ == '__main__':
    width, height = 3, 2
    state = random_state(width, height)
    print(state)
    #render(state)
    count_live_neighbors(state, (0, 1))
