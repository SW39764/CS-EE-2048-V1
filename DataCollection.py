import csv
import MCTSEnv
import GymTestingRLV1

header = ['Max Tile Size', 'Score']

runs = 20
MCTSIterations = 5

#MCTS
# with open('TestingDataCollectionMCTS.csv', 'w', encoding='UTF8') as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#
#     for _ in range(runs):
#         data = MCTSEnv.runner(1, 5)
#
#         writer.writerow(data)

#None
with open('TestingDataCollectionNN.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)

    for _ in range(runs):
        data = GymTestingRLV1.runner()

        writer.writerow(data)