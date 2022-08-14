import gym
import random

from GymEnv import MyGameEnv

env = MyGameEnv()


episodes = 10
for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    score = 0

    while not done:
        # env.render()
        action = env.action_space.sample()
        n_state, reward, done, info = env.step(action)
        score += reward
    print("Episode : {} Score : {}".format(episode, score))


# from GymGameLogic import *
#
# board = GameSave()
# board.printArr()
#
# while not board.gameOver():
#     board.moveLeft()
#     board.moveUp()
#     board.moveDown()
#     board.moveRight()
#
#     board.printArr()