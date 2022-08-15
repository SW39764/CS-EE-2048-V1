import gym
import numpy as np
import os
import matplotlib.pyplot as plt


import tensorflow as tf
# from tensorflow import keras

from keras import layers, models

from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy, LinearAnnealedPolicy, EpsGreedyQPolicy
from rl.memory import SequentialMemory


from GymEnv import MyGameEnv
from GymGameLogic import plotMaxs


env = MyGameEnv()

def build_model(states, actions):
    model = models.Sequential()

    model.add(layers.Conv2D(filters=16,kernel_size=3,padding="same",activation="relu",input_shape=(1,4,4)))
    model.add(layers.Conv2D(filters=32,kernel_size=2,padding="same",activation="relu"))
    model.add(layers.Flatten())
    model.add(layers.Dense(units=128, activation="relu"))
    model.add(layers.Dense(actions, activation='linear'))


    # model.add(layers.Flatten(input_shape=(1,4,4)))
    # model.add(layers.Dense(units=1024, activation="relu"))
    # model.add(layers.Dense(units=512, activation="relu"))
    # model.add(layers.Dense(units=256, activation="relu"))
    # model.add(layers.Dense(actions, activation='linear'))

    return model


states = env.observation_space.shape
actions = env.action_space.n

model = build_model(states, actions)
print(model.summary())

def build_agent(model, actions):
    # policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=1., value_min=1., value_test=0.1, nb_steps=1000)
    # memory = SequentialMemory(limit=5000, window_length=1)
    # dqn = DQNAgent(model=model, memory=memory, policy=policy, nb_actions=actions,nb_steps_warmup=1000, batch_size=200)

    memory = SequentialMemory(limit=5000, window_length=1)
    TRAIN_POLICY = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=0.05, value_min=0.05, value_test=0.01, nb_steps=1e5)

    dqn = DQNAgent(model=model, nb_actions=4, policy=TRAIN_POLICY, memory=memory, nb_steps_warmup=5000, gamma=.99, target_model_update=1000,
                   train_interval=4, delta_clip=1.)
    return dqn

# import visualkeras
# visualkeras.layered_view(model, to_file='output.png')

dqn = build_agent(model, actions)
dqn.compile(tf.keras.optimizers.Adam(lr=0.00025))
dqn.fit(env, nb_steps=500000, visualize=False, verbose=2)

plotMaxs()

model.save('model')

# model = models.load_model('model')