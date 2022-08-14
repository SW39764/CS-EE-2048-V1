import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
from tensorflow import keras

from keras import layers, models

from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory


from GymEnv import MyGameEnv


env = MyGameEnv()


def build_model(states, actions):
    model = models.Sequential()

    model.add(layers.Conv2D(filters=16,kernel_size=2,padding="same",activation="relu",input_shape=(1,4,4)))

    model.add(layers.Flatten())

    model.add(layers.Dense(24, activation='relu'))
    model.add(layers.Dense(24, activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(actions, activation='linear'))

    return model



states = env.observation_space.shape
actions = env.action_space.n

model = build_model(states, actions)
print(model.summary())

def build_agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=5000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy, nb_actions=actions,nb_steps_warmup=10, target_model_update=1e-2)
    return dqn

dqn = build_agent(model, actions)
dqn.compile(tf.keras.optimizers.Adam(lr=0.0003), metrics=["mae"])
dqn.fit(env, nb_steps=10000, visualize=False, verbose=1)


# print(env.observation_space.shape)