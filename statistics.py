import numpy as np   
def calculateStats(numbers):
  return None
 
def report_min_max_avg(a):
    a = np.array(a)
    computedStats = {}
    computedStats["min"] = a.min()
    computedStats["max"] = a.max()
    computedStats["avg"] = a.mean()
    return computedStats
