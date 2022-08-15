import numpy as np

from gym import Env
from gym.spaces import Discrete, Box

import matplotlib.pyplot as plt

from GymGameLogic import GameSave

class MyGameEnv(Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.action_space = Discrete(4)
        self.observation_space = Box(0, 16, [4,4,1], dtype=int)

        self.shape = 4,4
        self.move = 0

        self.state = GameSave()

    def step(self, action):
        if action == 0:
            self.state.moveLeft()
        if action == 1:
            self.state.moveRight()
        if action == 2:
            self.state.moveUp()
        if action == 3:
            self.state.moveDown()

        self.move += 1


        if self.state.gameOver():
            if self.state.getMax()==7:
                reward = 1
            else:
                reward = -1
            done = True
        else:
            done = False
            reward = 0

        info = {}

        return self.state.board, reward, done, info

    def render(self, mode = "human"):
        self.state.printArr()


    def reset(self):
        self.state = GameSave()
        self.move = 0

        return self.state.board