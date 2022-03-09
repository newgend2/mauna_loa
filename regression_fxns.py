##Contains Python functions for HW08, BDS 311
##These functions will be generated collaboratively and called in each user's separate Jupyter notebook

#import standard packages here


import numpy as np
from sklearn import linear_model

def make_standard_units(input_array):
    '''Converts input_array to standard_units, where data has mean 0 and standard deviation of 1
        INPUT: data array
        OUTPUT: array in standard units'''
    input_mean, input_stdev = np.mean(input_array), np.std(input_array) 
    return (input_array - input_mean)/input_stdev
    
    
def calc_corrcoef_from_standardized_input(array1,array2):
    '''Calculates Pearson correlation coefficient from two arrays in standard units
    INPUT: array1, array2: In standard units
    OUTPUT: Pearson correlation coefficient'''
    return np.corrcoef(array1, array2)[0,1]

def get_regression_parameters(array1, array2):
    '''Calculates regression parameters from two input arrays
    INPUT: array1, array2: two data arrays
    OUTPUT: regression_array, length 2: regression_array[0] is slope and regression_array[1] is intercept'''

    regr = linear_model.LinearRegression()
    X = array1.values.reshape(-1,1)
    y = array2
    regr.fit(X,y)
    regression_array = [regr.coef_[0], regr.intercept_]
    return regression_array


