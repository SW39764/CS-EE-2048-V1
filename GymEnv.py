#region IMPORTS

import random
from copy import deepcopy

import numpy as np

from gym import Env
from gym.spaces import Discrete, Box

import matplotlib.pyplot as plt

import GymGameLogic

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


def mergeRowL(row):
    for i in range(size - 1):
        for j in range(size-1, 0, -1):
            if row[i-1] == 0:
                row[i-1] = row[i]
                row[i] = 0
    for i in range(size - 1):
        if row[i] == row[i+1]:
            row[i] += 1
            row[i+1] = 0
    for i in range(size - 1, 0, -1):
        if row[i-1] == 0:
            row[i-1] = row[i]
            row[i] = 0
    return row

def moveLeft(b):
    for i in range(size):
        b[i] = mergeRowL(b[i])
    return b


def moveRight(n):
    return

def moveUp(n):
    return

def moveDown(n):
    return

max = 0
maxs = []

def gameOver(b):
    global max
    global maxs

    # same = b == moveUp(b).all() == moveDown(b).all() == moveRight(b).all() == moveLeft(b).all()
    # if same:
    #     num = getMax(b)
    #     if num > max:
    #         max = num
    #     maxs.append(num)
    #     print(num, "      ", max)
    #     printArr(b)

    return False

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
    # return getScore(n) + getMax(n) + getEmpty(n)*0.5 + it * 0.05
    return ((getMax(n) + (getScore(n)**0.5)/10)/10)

#endregion

class MyGameEnv(Env):
    metadata = {'render.modes': ['human']}

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


        if gameOver(self.state):
            done = True
        else:
            done = False

        if done:
            reward = -1
        else:
            reward = getReward(self.state, self.move)


        info = {}


        return self.state, reward, done, info

    def render(self, mode = "human"):
        printArr(self.state)
        # print("Render")


    def reset(self):
        board = np.zeros([4,4], dtype=np.uint8)
        addRandom(board, 2)

        self.state = board
        self.move = 0

        return self.state


def genplot():
    plt.plot(maxs)
    plt.show()