import random
from Game import *
from copy import deepcopy

mainGame = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
mainGame = addRandom(mainGame, 2)

iter = 30



def randomMove():
    pmoves = ["moveLeft", "moveRight", "moveUp", "moveDown"]
    choice = random.choice(pmoves)
    return(choice)


def runRandom(n):
    while (not gameOver(n)):

        chosen = randomMove() + "(n)"
        n = eval(chosen)
    return n

def oneIteration(inputGame):
    scoreLeft = 0
    scoreRight = 0
    scoreUp = 0
    scoreDown = 0

    emptyLeft = 0
    emptyRight = 0
    emptyUp = 0
    emptyDown = 0

    maxLeft = 0
    maxRight = 0
    maxUp = 0
    maxDown = 0

    for _ in range(iter):
        #left
        n = deepcopy(inputGame)
        n = moveLeft(n)
        n = runRandom(n)
        scoreLeft += getScore(n)
        maxLeft += getMax(n)
        emptyLeft += getEmpty(n)

        #right
        n = deepcopy(inputGame)
        n = moveRight(n)
        n = runRandom(n)
        scoreRight += getScore(n)
        maxRight += getMax(n)
        emptyRight += getEmpty(n)

        #up
        n = deepcopy(inputGame)
        n = moveUp(n)
        n = runRandom(n)
        scoreUp += getScore(n)
        maxUp += getMax(n)
        emptyUp += getEmpty(n)

        #down
        n = deepcopy(inputGame)
        n = moveDown(n)
        n = runRandom(n)
        scoreDown += getScore(n)
        maxDown += getMax(n)
        emptyDown += getEmpty(n)

    qualityLeft = (scoreLeft / iter)/2 + (maxLeft / iter)
    qualityRight = (scoreRight / iter)/2 + (maxRight / iter)
    qualityUp = (scoreUp / iter)/2 + (maxUp / iter)
    qualityDown = (scoreDown / iter)/2 + (maxDown / iter)


    # print(f"Average Left Score: {qualityLeft}")
    # print(f"Average Right Score: {qualityRight}")
    # print(f"Average Up Score: {qualityUp}")
    # print(f"Average Down Score: {qualityDown}")

    if qualityLeft > qualityRight and qualityLeft > qualityUp and qualityLeft > qualityDown:
        inputGame = moveLeft(inputGame)
    elif qualityRight > qualityLeft and qualityRight > qualityUp and qualityRight > qualityDown:
        inputGame = moveRight(inputGame)
    elif qualityUp > qualityLeft and qualityUp > qualityRight and qualityUp > qualityDown:
        inputGame = moveUp(inputGame)
    else:
        inputGame = moveDown(inputGame)
    return inputGame


if __name__ == '__main__':
    while (not gameOver(mainGame)):
        mainGame = oneIteration(mainGame)
        printArr(mainGame)
        print(getScore(mainGame))
