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
    """
    Calculate the distance from feature at start_index
    to all features in rest of the feature_list parameter
    :return 
    """
    closest_dist = 14142136  # maximum possible distance
    closest_feature = 'feature id'
    measure_start = start_index+1
    measure_end = len(feature_list)
    for i in range(measure_start, measure_end):
        feature_distance = calculate_distance(feature_list[start_index], feature_list[i])
        if feature_distance < closest_dist:
            closest_dist = feature_distance
            closest_feature = feature_list[i][0]
    return [closest_feature, str(closest_dist)]

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

