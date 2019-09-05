import numpy as np


def multiplicity_to_category(x):
    '''
    Translate multiplicity flag from MC into one-hot encoder 
    '''
    return {
        0: np.array([1, 0, 0, 0, 0]),
        1: np.array([0, 1, 0, 0, 0]),
        2: np.array([0, 0, 1, 0, 0]),
        3: np.array([0, 0, 0, 1, 0])
    }.get(x, np.array([0, 0, 0, 0, 1]))
