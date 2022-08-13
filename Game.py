import random
from copy import deepcopy

size = 4

def addRandom(n, i = 1):
    zeroes = False
    for y in n:
        for x in y:
            if x == 0:
                zeroes = True

    if not zeroes:
        return n

    for _ in range(i):
        while True:
            x = int(random.randint(0,3))
            y = int(random.randint(0,3))
            if n[x][y] == 0:
                n[x][y] = (random.choices([1,2], weights = (4,1)))[0]
                break
    return n

def printArr(n):
    for y in n:
        print(y)
    print()

def moveLeft(n):
    curr = deepcopy(n)
    for it in range(size):
        row = curr[it]
        for _ in range(size-1):
            for x in range(1, size):
                if row[x-1] == 0:
                    row[x-1] = row[x]
                    row[x] = 0

        for i in range(size - 1):
            if(row[i] == row[i+1]):
                row[i] += 1
                row[i+1] = 0

        for x in range(1, size):
            if row[x - 1] == 0:
                row[x - 1] = row[x]
                row[x] = 0

        curr[it] = row
    curr = addRandom(curr, 1)
    return curr

def moveRight(n):
    curr = deepcopy(n)
    for it in range(size):
        row = curr[it]
        for _ in range(size - 1):
            for x in range(size-2, -1, -1):
                if row[x + 1] == 0:
                    row[x + 1] = row[x]
                    row[x] = 0

        for i in range(size - 1, 0, -1):
            if (row[i] == row[i -1]):
                row[i] += 1
                row[i - 1] = 0

        for x in range(size - 2, -1, -1):
            if row[x + 1] == 0:
                row[x + 1] = row[x]
                row[x] = 0

        curr[it] = row
    curr = addRandom(curr, 1)
    return curr

def moveDown(n):
    curr = deepcopy(n)
    for it in range(size):
        col = [x[it] for x in curr]

        # print(f"\n{col}")

        for _ in range(size - 1):
            for x in range(size-2, -1, -1):
                if col[x + 1] == 0:
                    col[x + 1] = col[x]
                    col[x] = 0

        for i in range(size - 1, 0, -1):
            if (col[i] == col[i -1]):
                col[i] += 1
                col[i - 1] = 0

        for x in range(size - 2, -1, -1):
            if col[x + 1] == 0:
                col[x + 1] = col[x]
                col[x] = 0

        # print(f"{col}\n")

        for i, val in enumerate(col):
            curr[i][it] = val
    curr = addRandom(curr, 1)
    return curr

def moveUp(n):
    curr = deepcopy(n)
    for it in range(size):
        col = [x[it] for x in curr]

        # print(f"\n{col}")

        for _ in range(size - 1):
            for x in range(1, size):
                if col[x - 1] == 0:
                    col[x - 1] = col[x]
                    col[x] = 0

        for i in range(size - 1):
            if (col[i] == col[i + 1]):
                col[i] += 1
                col[i + 1] = 0

        for x in range(1, size):
            if col[x - 1] == 0:
                col[x - 1] = col[x]
                col[x] = 0

        # print(f"{col}\n")

        for i, val in enumerate(col):
            curr[i][it] = val

    curr = addRandom(curr, 1)
    return curr

def gameOver(n):

    return n == moveUp(n) and n == moveDown(n) and n == moveLeft(n) and n == moveRight(n)

def getScore(n):
    score = 0
    for row in n:
        for val in row:
            score += val**2
    return score

def getEmpty(n):
    empty = 0
    for row in n:
        for val in row:
            if val == 0:
                empty += 1
    return empty

def getMax(n):
    max = 0
    for row in n:
        for val in row:
            if val > max:
                max = val
    return max



if(__name__ == "__main__"):
    arr = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    arr = addRandom(arr, 12)

    printArr(arr)

    arr = moveUp(arr)

    printArr(arr)

