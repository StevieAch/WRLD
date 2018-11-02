'''
Created on 31 Oct 2018

@author: scmac
'''
import unittest
from wrld import calculate_distance
from wrld import find_features_shortest_distance

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
        test_feature00 = ['test_feature00', '1', '1']
        test_feature01 = ['test_feature01', '4', '5']
        
        output = calculate_distance(test_feature00, test_feature01)
        print('Expected: 5, actual: ' + str(output))
        
        self.assertEqual(5, output, 'Calculated distance incorrect')
        
class TestFindFeaturesShortestDistance(unittest.TestCase):
    
    def test_simple_shortest_distance(self):
        """
        Test using four primitive Pythagorean triples to 
        verify that the shortest distance is returned
        """
        test_feature00 = ['test_feature00', '1', '1'] # base coordinate
        test_feature01 = ['test_feature01', '6', '13'] # (5, 12) distance: 13
        test_feature02 = ['test_feature02', '9', '16'] # (8, 15) distance: 17
        test_feature03 = ['test_feature03', '4', '5'] # (3, 4) distance: 5 
        test_feature04 = ['test_feature04', '8', '25'] # (7, 24) distance: 25
        
        test_feature_list = [test_feature00, test_feature01, test_feature02,\
                             test_feature03, test_feature04]
        start_index = 0
        expected_output = ['test_feature03', '5.0']
        output = find_features_shortest_distance(start_index, test_feature_list)
        
        self.assertEqual(expected_output, output, 'Features shortest distance incorrect')
        print('Expected:',  expected_output, 'Actual:', output)
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()