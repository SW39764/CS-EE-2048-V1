import numpy as np

from gym import Env
from gym.spaces import Discrete, Box

import matplotlib.pyplot as plt

from GymGameLogic import GameSave

from copy import deepcopy

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

        # currState = deepcopy(self.state.board)

        if action == 0:
            self.state.moveLeft()
        elif action == 1:
            self.state.moveRight()
        elif action == 2:
            self.state.moveUp()
        else:
            self.state.moveDown()

        # if currState.all() == self.state.board.all():
        #     reward = -0.1

        if self.state.gameOver():
            done = True
            if self.state.getMax() > 7:
                reward = 1
            else:
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