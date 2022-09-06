from Environment import MyGameEnv
from Logic import GameSave
import numpy as np
from random import randint
from copy import deepcopy

#iterations also changed in data collection file
iter = 30
size = 4

env = MyGameEnv()

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
        scoresVals[0] += currentGame.state.score
        emptyVals[0] += currentGame.state.getEmpty()
        maxVals[0] += 2 ** currentGame.state.getMax()

        #right
        currentGame = deepcopy(env)
        currentGame.step(1)
        runRandom(currentGame)
        scoresVals[1] += currentGame.state.score
        emptyVals[1] += currentGame.state.getEmpty()
        maxVals[1] += 2 ** currentGame.state.getMax()

        #up
        currentGame = deepcopy(env)
        currentGame.step(2)
        runRandom(currentGame)
        scoresVals[2] += currentGame.state.score
        emptyVals[2] += currentGame.state.getEmpty()
        maxVals[2] += 2 ** currentGame.state.getMax()

        #down
        currentGame = deepcopy(env)
        currentGame.step(3)
        runRandom(currentGame)
        scoresVals[3] += currentGame.state.score
        emptyVals[3] += currentGame.state.getEmpty()
        maxVals[3] += 2 ** currentGame.state.getMax()

    qualityLeft = (scoresVals[0]) * checkNotIllegal(env, 0)
    qualityRight = (scoresVals[1]) * checkNotIllegal(env, 1)
    qualityUp = (scoresVals[2]) * checkNotIllegal(env, 2)
    qualityDown = (scoresVals[3]) * checkNotIllegal(env, 3)

    qualities = [qualityLeft, qualityRight, qualityUp, qualityDown]

    # print("\n")
    # print(qualities)

    tmp = max(qualities)
    best = qualities.index(tmp)
    # print(p_moves[best])

    # env.render()

    env.step(best)

def checkNotIllegal(save, direction):
    copy = deepcopy(save)
    if copy.state.move(direction) == "illegal":
        return False
    return True


if __name__ == "__main__":

    env.reset()

    while not env.state.gameOver():
        oneIteration()
        # print(env.state.score)
        # env.render()

    print("Finished with a score of", env.state.score, "and a max tile size of", 2 ** env.state.getMax())
    env.state.printArr()

def runner(iterations = 10):
    global iter
    iter = iterations

    env.reset()

    while not env.state.gameOver():
        oneIteration()

    env.render()
    print(env.state.getMax())
    print("Finished with a score of", env.state.score, "and a max tile size of", (2 ** env.state.getMax()))
    # env.state.printArr()

    return([2**env.state.getMax(), env.state.score])