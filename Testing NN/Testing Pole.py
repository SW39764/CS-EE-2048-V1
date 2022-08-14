import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import gym
import numpy as np

import tensorflow as tf
from tensorflow import keras
from keras import models, layers

from rl.policy import BoltzmannQPolicy, LinearAnnealedPolicy, EpsGreedyQPolicy
from rl.agents import DQNAgent
from rl.memory import SequentialMemory

env = gym.make("CartPole-v1")


def build_model(states, actions):
    model = models.Sequential()
    model.add(layers.Flatten(input_shape=states))
    model.add(layers.Dense(units=512, activation="relu"))
    model.add(layers.Dense(units=128, activation="relu"))
    model.add(layers.Dense(actions, activation='linear'))

    return model


states = env.observation_space.shape
actions = env.action_space.n

model = build_model(states, actions)
print(model.summary())

def build_agent(model, actions):
    policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=1., value_min=.1, value_test=0.1, nb_steps=5000)
    memory = SequentialMemory(limit=5000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy, nb_actions=actions,nb_steps_warmup=1000, batch_size=200)
    return dqn

# dqn = build_agent(model, actions)
# dqn.compile(tf.keras.optimizers.Adam(lr=0.005))
# dqn.fit(env, nb_steps=1000000, visualize=False, verbose=2)

env.render