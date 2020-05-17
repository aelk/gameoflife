from random import randint

def dead_state(width, height):
    return [[0] * width] * height

def random_state(width, height):
    state = dead_state(width, height)
    for i in range(height):
        for j in range(width):
            state[i][j] = randint(0, 1)
    return state

if __name__ == '__main__':
    width = 3
    height = 5
    print("width =", width)
    print("height =", height)
    state = random_state(width, height)
    print(state)
