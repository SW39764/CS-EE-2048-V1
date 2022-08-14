#region IMPORTS

import random
from copy import deepcopy

import numpy as np

from gym import Env
from gym.spaces import Discrete, Box

import matplotlib.pyplot as plt

#endregion

#region SETTINGS

size = 4

#endregion

#region LOGIC
def addRandom(n, i=1):
    zeroes = False
    for y in n:
        for x in y:
            if x == 0:
                zeroes = True

    if not zeroes:
        return n

    for _ in range(i):
        while True:
            x = int(random.randint(0, 3))
            y = int(random.randint(0, 3))
            if n[x][y] == 0:
                n[x][y] = (random.choices([1, 2], weights=(4, 1)))[0]
                break
    return n

def printArr(n):
    for y in n:
        print(y)
    print()

def moveLeft(n):
    curr = deepcopy(n)
    for it in range(size):
        row = curr[it]
        for _ in range(size - 1):
            for x in range(1, size):
                if row[x - 1] == 0:
                    row[x - 1] = row[x]
                    row[x] = 0

        for i in range(size - 1):
            if (row[i] == row[i + 1]):
                row[i] += 1
                row[i + 1] = 0

        for x in range(1, size):
            if row[x - 1] == 0:
                row[x - 1] = row[x]
                row[x] = 0

        curr[it] = row
    curr = addRandom(curr, 1)
    return curr

def moveRight(n):
    curr = deepcopy(n)
    for it in range(size):
        row = curr[it]
        for _ in range(size - 1):
            for x in range(size - 2, -1, -1):
                if row[x + 1] == 0:
                    row[x + 1] = row[x]
                    row[x] = 0

        for i in range(size - 1, 0, -1):
            if (row[i] == row[i - 1]):
                row[i] += 1
                row[i - 1] = 0

        for x in range(size - 2, -1, -1):
            if row[x + 1] == 0:
                row[x + 1] = row[x]
                row[x] = 0

        curr[it] = row
    curr = addRandom(curr, 1)
    return curr

def moveDown(n):
    curr = deepcopy(n)
    for it in range(size):
        col = [x[it] for x in curr]

        # print(f"\n{col}")

        for _ in range(size - 1):
            for x in range(size - 2, -1, -1):
                if col[x + 1] == 0:
                    col[x + 1] = col[x]
                    col[x] = 0

        for i in range(size - 1, 0, -1):
            if (col[i] == col[i - 1]):
                col[i] += 1
                col[i - 1] = 0

        for x in range(size - 2, -1, -1):
            if col[x + 1] == 0:
                col[x + 1] = col[x]
                col[x] = 0

        # print(f"{col}\n")

        for i, val in enumerate(col):
            curr[i][it] = val
    curr = addRandom(curr, 1)
    return curr

def moveUp(n):
    curr = deepcopy(n)
    for it in range(size):
        col = [x[it] for x in curr]

        # print(f"\n{col}")

        for _ in range(size - 1):
            for x in range(1, size):
                if col[x - 1] == 0:
                    col[x - 1] = col[x]
                    col[x] = 0

        for i in range(size - 1):
            if (col[i] == col[i + 1]):
                col[i] += 1
                col[i + 1] = 0

        for x in range(1, size):
            if col[x - 1] == 0:
                col[x - 1] = col[x]
                col[x] = 0

        # print(f"{col}\n")

        for i, val in enumerate(col):
            curr[i][it] = val

    curr = addRandom(curr, 1)
    return curr

max = 0
maxs = []

def gameOver(n):
    global max
    global maxs
    if (n == moveUp(n)).all() and (n == moveDown(n)).all() and (n == moveLeft(n)).all() and (n == moveRight(n)).all():
        num = getMax(n)
        if num > max:
            max = num
        maxs.append(num)
        print(num, "      ", max)

    return (n == moveUp(n)).all() and (n == moveDown(n)).all() and (n == moveLeft(n)).all() and (n == moveRight(n)).all()

def getScore(n):
    score = 0
    for row in n:
        for val in row:
            score += val ** 2
    return score

def getEmpty(n):
    empty = 0
    for row in n:
        for val in row:
            if val == 0:
                empty += 1
    return empty

def getMax(n):
    max = 0
    for row in n:
        for val in row:
            if val > max:
                max = val
    return max

def getReward(n, it):
    return getScore(n) + getMax(n) + getEmpty(n)*0.5 + it * 0.05

#endregion

class MyGameEnv(Env):

    def __init__(self):
        self.action_space = Discrete(4)
        self.observation_space = Box(0, 16, [4,4,1], dtype=int)
        self.shape = 4,4
        self.move = 0

        board = np.zeros([4,4], dtype=np.uint8)
        addRandom(board, 2)


        self.state = board

    def step(self, action):
        if action == 0:
            self.state = moveLeft(self.state)
        if action == 1:
            self.state = moveRight(self.state)
        if action == 2:
            self.state = moveUp(self.state)
        if action == 3:
            self.state = moveDown(self.state)

        self.move += 1

        reward = getReward(self.state, self.move)

        if gameOver(self.state):
            done = True
        else:
            done = False

        info = {}


        return self.state, reward, done, info

    def render(self):
        printArr(self.state)

    def reset(self):
        board = np.zeros([4,4], dtype=np.uint8)
        addRandom(board, 2)

        self.state = board

        self.move = 0

        return self.state


def genplot():
    plt.plot(maxs)
    plt.show()