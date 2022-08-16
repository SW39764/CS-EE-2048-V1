from GymEnv import MyGameEnv
import numpy as np
from random import randint
from copy import deepcopy

iter = 10
size = 4

def getRandomMove():
    return randint(0,3)

def runRandom(game):
    while not game.state.gameOver():
        game.step(getRandomMove())
        # game.render()

def oneIteration():
    scores = [0,0,0,0]
    empty = [0,0,0,0]
    max = [0,0,0,0]

    for _ in range(iter):
        #left
        currentGame = deepcopy(env)
        currentGame.step(0)
        runRandom(currentGame)
        scores[0] += currentGame.state.getScore()
        empty[0] += currentGame.state.getEmpty()
        max[0] += currentGame.state.getMax()

        #right
        currentGame = deepcopy(env)
        currentGame.step(1)
        runRandom(currentGame)
        scores[1] += currentGame.state.getScore()
        empty[1] += currentGame.state.getEmpty()
        max[1] += currentGame.state.getMax()

        #up
        currentGame = deepcopy(env)
        currentGame.step(2)
        runRandom(currentGame)
        scores[2] += currentGame.state.getScore()
        empty[2] += currentGame.state.getEmpty()
        max[2] += currentGame.state.getMax()

        #down
        currentGame = deepcopy(env)
        currentGame.step(3)
        runRandom(currentGame)
        scores[3] += currentGame.state.getScore()
        empty[3] += currentGame.state.getEmpty()
        max[3] += currentGame.state.getMax()**2

    qualityLeft = (scores[0] + max[0]) / iter
    qualityRight = (scores[1] + max[1]) / iter
    qualityUp = (scores[2] + max[2]) / iter
    qualityDown = (scores[3] + max[3]) / iter

    if qualityLeft > qualityRight and qualityLeft > qualityUp and qualityLeft > qualityDown:
        env.step(0)
    elif qualityRight > qualityDown and qualityRight > qualityUp:
        env.step(1)
    elif qualityUp > qualityDown:
        env.step(2)
    else:
        env.step(3)

    print("\n\n\n")
    print(f"Average Left Quality: {qualityLeft}")
    print(f"Average Right Quality: {qualityRight}")
    print(f"Average Up Quality: {qualityUp}")
    print(f"Average Down Quality: {qualityDown}")

if __name__ == "__main__":
    env = MyGameEnv()

    while not env.state.gameOver():
        oneIteration()
        # print(env.state.score)
        env.render()