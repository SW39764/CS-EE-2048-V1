import numpy as np

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
    # model.add(Conv2D(64, (3, 3), padding="same", activation="relu", input_shape=(1,4,4)))
    # model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(layers.Dense(24, activation='relu', input_shape=states))
    model.add(layers.Dense(24, activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(actions, activation='linear'))
    return model



states = env.observation_space.shape
actions = env.action_space.n




model = models.Sequential([
    (layers.Flatten(input_shape=(1,4,4))),
    (layers.Dense(24, activation='relu')),
    (layers.Dense(24, activation='relu')),
    (layers.Dense(actions, activation='linear'))
])


# model = build_model()
print(model.summary())

def build_agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=5000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy, nb_actions=actions,nb_steps_warmup=10, target_model_update=1e-2)
    return dqn

dqn = build_agent(model, actions)
dqn.compile(tf.keras.optimizers.Adam(lr=0.0001), metrics=["mae"])
dqn.fit(env, nb_steps=6000, visualize=False, verbose=1)


# print(env.observation_space.shape)