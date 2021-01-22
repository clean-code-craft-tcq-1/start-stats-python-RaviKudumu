import numpy as np   
def calculateStats(numbers):
  return None
 
def report_min_max_avg(a):
    a = np.array(a)
    dict_stat = {}
    dict_stat["min"] = a.min()
    dict_stat["max"] = a.max()
    dict_stat["avg"] = a.mean()
    return dict_stat
