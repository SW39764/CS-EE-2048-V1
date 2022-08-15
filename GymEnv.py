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
        self.move += 1

        reward = 0

        if action == 0:
            reward = self.state.moveLeft()
        elif action == 1:
            reward = self.state.moveRight()
        elif action == 2:
            reward = self.state.moveUp()
        else:
            reward = self.state.moveDown()

        if self.state.gameOver():
            done = True
            if self.state.getMax() < 7:
                reward = -1
        else:
            done = False

        info = {}
        return self.state.board, reward, done, info

    def render(self, mode = "human"):
        self.state.printArr()


    def reset(self):
        self.state = GameSave()
        self.move = 0

        return self.state.board