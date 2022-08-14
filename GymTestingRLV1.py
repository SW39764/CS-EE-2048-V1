import keras as keras
import numpy as np

import keras
import tensorflow as tf

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from keras.optimizers import Adam

from keras import layers
from keras import layers, models

from GymEnv import MyGameEnv

from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory


env = MyGameEnv()


def build_model(states, actions):
    model = Sequential()
    # model.add(Conv2D(64, (3, 3), padding="same", activation="relu", input_shape=(1,4,4)))
    # model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dense(24, activation='relu', input_shape=states))
    model.add(Dense(24, activation='relu'))
    model.add(Flatten())
    model.add(Dense(actions, activation='linear'))
    return model



states = env.observation_space.shape
actions = env.action_space.n


####

def build_model(board_size=4, board_layers=16, outputs=4, filters=64, residual_blocks=4):
    # Functional API model
    inputs = layers.Input(shape=(board_size * board_size * board_layers,))
    x = layers.Reshape((board_size, board_size, board_layers))(inputs)

    # Initial convolutional block
    x = layers.Conv2D(filters=filters, kernel_size=(3, 3), padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)

    # residual blocks
    for i in range(residual_blocks):
        # x at the start of a block
        temp_x = layers.Conv2D(filters=filters, kernel_size=(3, 3), padding='same')(x)
        temp_x = layers.BatchNormalization()(temp_x)
        temp_x = layers.Activation('relu')(temp_x)
        temp_x = layers.Conv2D(filters=filters, kernel_size=(3, 3), padding='same')(temp_x)
        temp_x = layers.BatchNormalization()(temp_x)
        x = layers.add([x, temp_x])
        x = layers.Activation('relu')(x)

    # policy head
    x = layers.Conv2D(filters=2, kernel_size=(1, 1), padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    x = layers.Flatten()(x)
    predictions = layers.Dense(outputs, activation='softmax')(x)

    # Create model
    return models.Model(inputs=inputs, outputs=predictions)


###


model = build_model()
print(model.summary())

def build_agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=5000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy, nb_actions=actions,
                   nb_steps_warmup=10, target_model_update=1e-2)
    return dqn

dqn = build_agent(model, actions)
dqn.compile(Adam(lr=0.0001), metrics=["mae"])
dqn.fit(env, nb_steps=60, visualize=False, verbose=1)


# print(env.observation_space.shape)