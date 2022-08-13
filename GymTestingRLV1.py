import numpy as np

import keras
import tensorflow

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Flatten, Conv2D
from keras.optimizers import Adam

from GymEnv import MyGameEnv


from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory



env = MyGameEnv()



def build_model(states, actions):
    model = Sequential()
    # model.add(Conv2D(255, (3, 3), activation='relu', input_shape=(4, 4, 1)))
    model.add(Dense(24, activation='relu', input_shape=(1,4,4)))
    model.add(Dense(24, activation='relu'))
    model.add(Flatten())
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
                   nb_steps_warmup=5, target_model_update=1e-2)
    return dqn

dqn = build_agent(model, actions)
dqn.compile(Adam(lr=1e-3), metrics=["mae"])
dqn.fit(env, nb_steps=6000, visualize=False, verbose=1)