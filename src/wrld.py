'''
Created on 31 Oct 2018

@author: scmac
'''
import math

def load_start():
    """
    Load initial values from file
    """
    input_file = 'input//problem_small.txt'
    try:
        with open(input_file) as in_file:
            feature_list = [i.rstrip('\n').split(' ') for i in in_file]
        for i in feature_list:
            print(i)

        return feature_list
    except IOError:
        print('Input file could not be accessed.')

def find_features_shortest_distance(start_index, feature_list):
    pass

def calculate_distance(current_feature, other_feature):
    """
    Calculate the distance between the two 
    parameter features via Pythagoras' Theorem
    """
    delta_x = abs(int(current_feature[1]) - int(other_feature[1]))
    delta_y = abs(int(current_feature[2]) - int(other_feature[2]))
    return math.sqrt(delta_x**2 + delta_y**2)

if __name__ == '__main__':
    pass

load_start()