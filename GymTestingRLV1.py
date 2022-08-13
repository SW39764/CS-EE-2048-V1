import numpy as np

import keras
import tensorflow

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Flatten
from keras.optimizers import Adam

from GymEnv import MyGameEnv


from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory



env = MyGameEnv()



def build_model(states, actions):
    model = Sequential()
    model.add(Dense(24, activation='relu', input_shape=(9,)))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(actions, activation='linear'))
    return model

states = env.observation_space.shape
actions = env.action_space.n

model = build_model(states, actions)
print(model.summary())



def build_agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=5000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy, nb_actions=actions,
                   nb_steps_warmup=10, target_model_update=1e-2)
    return dqn

dqn = build_agent(model, actions)
dqn.compile(Adam(lr=1e-3), metrics=["mae"])
dqn.fit(env, nb_steps=50000, visualize=False, verbose=1)