import csv


with open('TestingDataCollectionMCTS.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(["Column 1", "Column 2"])

    for _ in range(12):
        writer.writerow([_, _+1])