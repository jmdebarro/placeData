import sys, csv, os
import time
from datetime import datetime
from collections import defaultdict
from time import perf_counter_ns


# Populates dictionaries from CSV
def analyzeCSV(colorQuantity, coordQuantity, starDate, endDate):
    pathName = os.path.join(os.getcwd(), 'placeData.csv')
    print(f"{pathName}\n")

    with open(pathName, newline='') as file:
        csvReader = csv.reader(file, delimiter=',')
        # Skips header
        csvReader.__next__()
        # Iterate through csv and add values to dictionary
        counter = 0
        for row in csvReader:
            date = datetime.strptime(row[0].split(":")[0], "%Y-%m-%d %H")
            if date < starDate or date >= endDate:
                continue
            color = row[2]
            coord = row[3]
            # print(f"{date} \n {color} \n {coord}")
            # time.sleep(2)
            if counter % 100 == 0:
                print(f"{date} {color} {coord}")

            colorQuantity[color] += 1
            coordQuantity[coord] += 1
            counter += 1


# Find the value with the maximum occurrences
def findTopValue(pixelDict):
    maxVal = 0
    maxKey = "N/A"

    if not pixelDict:
        return "No values in given time frame"
    for key, value in pixelDict.items():
        if value > maxVal:
            maxVal = value
            maxKey = key
    
    return maxKey


def main(args):

    # Start timer
    start = perf_counter_ns() 

    print(args)
    # Start and end date given via sys.argv
    startDate = datetime.strptime(args[1], '%Y-%m-%d %H')
    endDate = datetime.strptime(args[2], '%Y-%m-%d %H')

    if endDate < startDate:
        print("End date must be greather than start")
        return Exception("End date is less than start date")

    # Maps to record pixel palcement and color amounts
    colorQuantity = defaultdict(lambda: 0)
    coordQuantity = defaultdict(lambda: 0)

    analyzeCSV(colorQuantity, coordQuantity, startDate, endDate)

    topColor = findTopValue(colorQuantity)
    topCoord = findTopValue(coordQuantity)

    # End timer
    stop = perf_counter_ns() 
    executionTime = stop - start

    print(f"Timeframe: {startDate} to {endDate}")
    print(f"Execution Time: {executionTime}")
    print(f"Most Placed Color: {topColor}")
    print(f"Most Place Pixel Location: {topCoord}")

if __name__ == '__main__':
    main(sys.argv)
