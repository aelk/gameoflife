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
    for row in state:
        print(row)
    '''
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 0:
                print(" ")
            else:
                print("#")
    '''

if __name__ == '__main__':
    width, height = 3, 5
    state = random_state(width, height)
    print(state)
    render(state)
