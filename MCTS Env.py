from GymEnv import MyGameEnv
from GymGameLogic import GameSave
import numpy as np
from random import randint
from copy import deepcopy
import operator

iter = 30
size = 4

p_moves = ["Left", "Right", "Up", "Down"]

def getRandomMove():
    return randint(0,3)

def runRandom(game):
    while not game.state.gameOver():
        game.step(getRandomMove())
        # game.render()

def oneIteration():
    scoresVals = [0,0,0,0]
    emptyVals = [0,0,0,0]
    maxVals = [0,0,0,0]


    for _ in range(iter):
        #left
        currentGame = deepcopy(env)
        currentGame.step(0)
        runRandom(currentGame)
        scoresVals[0] += currentGame.state.getScore()
        emptyVals[0] += currentGame.state.getEmpty()
        maxVals[0] += currentGame.state.getMax()

        #right
        currentGame = deepcopy(env)
        currentGame.step(1)
        runRandom(currentGame)
        scoresVals[1] += currentGame.state.getScore()
        emptyVals[1] += currentGame.state.getEmpty()
        maxVals[1] += currentGame.state.getMax()

        #up
        currentGame = deepcopy(env)
        currentGame.step(2)
        runRandom(currentGame)
        scoresVals[2] += currentGame.state.getScore()
        emptyVals[2] += currentGame.state.getEmpty()
        maxVals[2] += currentGame.state.getMax()

        #down
        currentGame = deepcopy(env)
        currentGame.step(3)
        runRandom(currentGame)
        scoresVals[3] += currentGame.state.getScore()
        emptyVals[3] += currentGame.state.getEmpty()
        maxVals[3] += currentGame.state.getMax()**2
    qualityLeft = ((scoresVals[0] + maxVals[0]) / iter) * checkNotIllegal(env, 0)
    qualityRight = ((scoresVals[1] + maxVals[1]) / iter) * checkNotIllegal(env, 1)
    qualityUp = ((scoresVals[2] + maxVals[2]) / iter) * checkNotIllegal(env, 2)
    qualityDown = ((scoresVals[3] + maxVals[3]) / iter) * checkNotIllegal(env, 3)

    qualities = [qualityLeft, qualityRight, qualityUp, qualityDown]

    print("\n")

    print(qualities)

    tmp = max(qualities)
    best = qualities.index(tmp)
    print(p_moves[best])

    env.render()

    env.step(best)

def checkNotIllegal(save, direction):
    copy = deepcopy(save)
    if copy.state.move(direction) == "illegal":
        print("Illegal")
        return False
    return True


if __name__ == "__main__":
    env = MyGameEnv()

    while not env.state.gameOver():
        oneIteration()
        # print(env.state.score)
        # env.render()