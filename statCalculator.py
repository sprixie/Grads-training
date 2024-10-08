import numpy as np
from utils import *

class StatisticalCalculator:
    def __init__(self, data):
        self.data = np.array(data)  # Store data as a numpy array

    def mean(self):
        if len(self.data) == 0:
            return None
        else:
            return sum(self.data) / len(self.data)

    def sampleVariance(self):
        if len(self.data) < 2: # Not enough data for sample variance
            return None  
        mean_val = self.mean()
        return np.sum((self.data - mean_val) ** 2) / (len(self.data) - 1)

    def standardDeviation(self):
        var = self.sampleVariance()
        return np.sqrt(var) if var is not None else None

    def median(self):
        if len(self.data) == 0:
            return None
        else:
            sorted_data = np.sort(self.data)  # Use numpy's sort
            index = len(sorted_data) // 2
            if len(sorted_data) % 2 == 0:
                return (sorted_data[index-1] + sorted_data[index]) / 2
            else:
                return sorted_data[index]

