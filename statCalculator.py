import numpy as np
from utils import *

class StatisticalCalculator:
    def __init__(self, data):
        self.mean = self.mean(data)
        self.sampleVariance = self.sampleVariance(data)
        self.standardDeviation = self.standardDeviation(data)
        self.median = self.median(data)

    def mean(self, data):
        if len(data) == 0:
            return None
        else:
            return sum(data) / len(data)
        
    def sampleVariance(self, data):
        if len(data) == 0:
            return None
        else:
            return sum((data-self.mean)**2) / (len(data)-1) 

    def standardDeviation(self, data):
        if len(data) == 0:
            return None
        else:
            return np.sqrt(self.sampleVariance)
        
    def median(self, data):
        if len(data) == 0:
            return None
        else:
            sortedData = np.array(quicksort(list(data)))
            index = int(len(sortedData) // 2)
            if len(sortedData) % 2 == 0:
                return (sortedData[index-1] + sortedData[index])/2
            else:
                return sortedData[index]
        