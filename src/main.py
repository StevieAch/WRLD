'''
Created on 31 Oct 2018

@author: scmac
'''


def load_start():
    """
    Load initial values from file
    """
    print('load_start accessed')
    input_file = 'input//problem_small.txt'
    try:
        with open(input_file) as in_file:
            feature_list = [i.rstrip('\n').split(' ') for i in in_file]
        print (feature_list)
        return feature_list
    except IOError:
        print('Input file could not be accessed.')
    
if __name__ == '__main__':
    pass

features = load_start()
