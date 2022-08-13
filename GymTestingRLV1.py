import keras as keras
import numpy as np

import keras
import tensorflow as tf

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from keras.optimizers import Adam

from GymEnv import MyGameEnv


from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory


env = MyGameEnv()


def build_model(states, actions):
    model = Sequential()
    # model.add(Conv2D(64, (3, 3), padding="same", activation="relu", input_shape=(1,4,4)))
    # model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dense(24, activation='relu', input_shape=(1,4,4)))
    model.add(Dense(24, activation='relu'))
    model.add(Flatten())
    model.add(Dense(actions, activation='linear'))
    return model

states = env.observation_space.shape
actions = env.action_space.n


# tf.compat.v1.disable_eager_execution()
# session = keras.backend.get_session()
# init = tf.compat.v1.global_variables_initializer()
# session.run(init)

# from tensorflow.python.framework.ops import disable_eager_execution
# disable_eager_execution()

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
dqn.fit(env, nb_steps=6000, visualize=False, verbose=1)