'''
Created on 31 Oct 2018

@author: scmac
'''
import unittest
from main import calculate_distance 

class TestCalculateDistance(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_calculate_distance(self):
        """
        Happy path 3,4,5 triangle
        Distance = 5
        """
        test_feature01 = ['test_feature01', '1', '1']
        test_feature02 = ['test_feature02', '4', '5']
        
        self.assertEqual(5, calculate_distance(test_feature01, test_feature02), 'Calculated distance incorrect')
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()