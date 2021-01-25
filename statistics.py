import numpy as np   
def calculateStats(numbers):
    computedStats = {}
    if numbers == []:
        computedStats["min"] = float('nan')
        computedStats["max"] = float('nan')
        computedStats["avg"] = float('nan')
    else:
        numbers = np.array(numbers)
        computedStats["min"] = numbers.min()
        computedStats["max"] = numbers.max()
        computedStats["avg"] = numbers.mean()
    return computedStats
