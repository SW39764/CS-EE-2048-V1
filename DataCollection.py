import csv
import MCTS
import CNN

header = ['Max Tile Size', 'Score']

runs = 20
MCTSIterations = 5

# MCTS
with open('TestingDataCollectionMCTS.csv', 'w', encoding='UTF8', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)

    for _ in range(runs):
        data = MCTS.runner(MCTSIterations)

        writer.writerow(data)

#None
with open('TestingDataCollectionNN.csv', 'w', encoding='UTF8', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)

    for _ in range(runs):
        data = CNN.runner()

        writer.writerow(data)