import numpy as np
import os
import matplotlib.pyplot as plt

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
from tensorflow import keras



from keras import layers, models

from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy, LinearAnnealedPolicy, EpsGreedyQPolicy
from rl.memory import SequentialMemory


from GymEnv import MyGameEnv, genplot


env = MyGameEnv()


def build_model(states, actions):
    model = models.Sequential()

    model.add(layers.Conv2D(filters=4,kernel_size=3,padding="same",activation="relu",input_shape=(1,4,4)))
    model.add(layers.Conv2D(filters=4,kernel_size=2,padding="same",activation="relu"))
    # model.add(layers.Conv2D(filters=4,kernel_size=3,padding="same",activation="relu"))

    model.add(layers.Flatten())

    model.add(layers.Dense(12, activation='relu'))
    model.add(layers.Dense(actions, activation='linear'))

    return model


states = env.observation_space.shape
actions = env.action_space.n

model = build_model(states, actions)
print(model.summary())

def build_agent(model, actions):
    policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=1., value_min=0.1, value_test=0.1, nb_steps=1000)
    memory = SequentialMemory(limit=50000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy, nb_actions=actions,nb_steps_warmup=1000, target_model_update=1e-2)
    return dqn

# import visualkeras
# visualkeras.layered_view(model, to_file='output.png')

dqn = build_agent(model, actions)
dqn.compile(tf.keras.optimizers.Adam(lr=1e-2))
dqn.fit(env, nb_steps=10000, visualize=False, verbose=2)

genplot()