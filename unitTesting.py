import unittest
import numpy as np
from statCalculator import *

class unitTester(unittest.TestCase):
    def testEmptyArray(self):
        """
        Test case for empty input array.
        """
        input = StatisticalCalculator(np.array([])) 
        self.assertEqual(input.mean, None)
        self.assertEqual(input.sampleVariance, None)
        self.assertEqual(input.standardDeviation, None)

    def testSameValueArray(self):
        """
        Test case for input array with the same values.
        """
        input = StatisticalCalculator(np.ones(3)) 
        self.assertEqual(input.mean, 1)
        self.assertEqual(input.sampleVariance, 0)
        self.assertEqual(input.standardDeviation, 0)
        self.assertEqual(input.median, 1)

    def testMedian(self):
        """
        Test cases for median.
        """
        input = StatisticalCalculator(np.array([9,3,6,7,8,1,3])) 
        self.assertEqual(input.median, 6)
        input = StatisticalCalculator(np.array([8,6,4,5,1,2,3,9])) 
        self.assertEqual(input.median, 4.5)

if __name__ == '__main__':
    unittest.main()