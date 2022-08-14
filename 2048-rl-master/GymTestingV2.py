import gym
import random
import sys


from gym2048 import Env2048

env = Env2048()

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