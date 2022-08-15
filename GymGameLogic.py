import  numpy as np
import random
import copy
import matplotlib.pyplot as plt

global maxs
maxs = []

def plotMaxs():
    plt.plot(maxs)
    plt.show()

class GameSave:
    def __init__(self, size = 4):
        self.size = size
        self.board = np.zeros([size, size], dtype=np.uint8)
        self.addRandom(2)
        self.maxReward = 7

    def addRandom(self, i=1):
        zeroes = False
        for y in self.board:
            for x in y:
                if x == 0:
                    zeroes = True

        if not zeroes:
            return self.board

        for _ in range(i):
            while True:
                x = int(random.randint(0, 3))
                y = int(random.randint(0, 3))
                if self.board[x][y] == 0:
                    self.board[x][y] = (random.choices([1, 2], weights=(4, 1)))[0]
                    break

    def printArr(self):
        for y in self.board:
            print(y)
        print()

    def mergeRowL(self, row):
        for i in range(self.size - 1):
            for j in range(self.size - 1, 0, -1):
                if row[j - 1] == 0:
                    row[j - 1] = row[j]
                    row[j] = 0
        for i in range(self.size - 1):
            if row[i] == row[i + 1]:
                if row[i] != 0 :
                    row[i] += 1
                    row[i + 1] = 0
        for i in range(self.size - 1, 0, -1):
            if row[i - 1] == 0:
                row[i - 1] = row[i]
                row[i] = 0
        return row

    def moveLeft(self):
        for i in range(self.size):
            self.board[i] = self.mergeRowL(self.board[i])

        self.addRandom()

    def moveRight(self):
        for i in range(self.size):
            arr = self.board[i]
            arr = arr[::-1]
            arr = self.mergeRowL(arr)
            arr = arr[::-1]
            self.board[i] = arr

        self.addRandom()

    def moveUp(self):
        self.board = self.board.transpose()
        for i in range(self.size):
            arr = self.board[i]
            arr = self.mergeRowL(arr)
            self.board[i] = arr
        self.board = self.board.transpose()

        self.addRandom()

    def moveDown(self):
        self.board = self.board.transpose()
        for i in range(self.size):
            arr = self.board[i]
            arr = arr[::-1]
            arr = self.mergeRowL(arr)
            arr = arr[::-1]
            self.board[i] = arr
        self.board = self.board.transpose()

        self.addRandom()

    def gameOver(self):
        for row in self.board:
            for i in range(self.size-1):
                if row[i] == row[i+1]:
                    return False
        for column in self.board.transpose():
            for i in range(self.size-1):
                if column[i] == column[i+1]:
                    return False
        for row in self.board:
            for n in row:
                if n == 0:
                    return False
        max = self.getMax()
        print(max)
        maxs.append(max)
        # self.printArr()
        return True

    def getScore(self):
        score = 0
        for row in self.board:
            for val in row:
                score += val ** 2
        return score

    def getEmpty(self):
        empty = 0
        for row in self.board:
            for val in row:
                if val == 0:
                    empty += 1
        return empty

    def getMax(self):
        max = 0
        for row in self.board:
            for val in row:
                if val > max:
                    max = val
        return max

    def getReward(self):
        return