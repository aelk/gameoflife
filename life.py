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

def next_board_state(state):
    # TODO
    return state

if __name__ == '__main__':
    width, height = 37, 28
    state = random_state(width, height)
    print(state)
    render(state)
