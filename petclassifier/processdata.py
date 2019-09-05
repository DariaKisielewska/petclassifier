import uproot
import uproot_methods
import numpy as np
import pandas as pd
import time


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


def change_to_category(table):
    tab = []
    for i in range(table.shape[0]):
        tab.append(np.argmax(table[i]))
    return np.array(tab)


def prepare_mc_sliding_window(tree, evts_in_half_window, num_of_categories):
    ''' Function prepares data in a sliding window format for further ML processing. 
    Output is prepared for many-to-one learning scheme. Event is surrounded by its neighbours 
    (given by evts_in_half_window) on both sides. Output is adjusted to one-hot encoding scheme,
    where number of categories is given by num_of_categories.
    '''

    time_start = time.time()

    # event to classify will be delivered with its neighbours
    window = 2*evts_in_half_window+1

    # get features and result from ROOT's tree. Parameters are fixed for now.
    raw_result = tree.pandas.df(
        ["fMCHits.fGenGammaMultiplicity"]).dropna(axis=0).values
    raw_features = tree.pandas.df(
        ["fMCHits.fTime", "fMCHits.fEneDep", "fMCHits.fPosition"]).dropna(axis=0).values

    time_process = time.time()

    out_features = np.empty(
        (raw_features.shape[0]-window, window, raw_features.shape[1]))
    out_results = np.empty(
        (raw_features.shape[0]-window, 1, raw_features.shape[1]))
    raw_categorical_results = np.empty(
        (raw_features.shape[0], num_of_categories))

    for i in range(raw_result.shape[0]):
        raw_categorical_results[i] = multiplicity_to_category(raw_result[i][0])

    for i in range(raw_features.shape[0]-window):
        out_features[i] = raw_features[i:i+window, :]
        out_results[i] = raw_categorical_results[i+evts_in_half_window]

    for i in range(out_features.shape[0]):
        for j in range(window):
            out_features[i, j, 0] = out_features[i,
                                                 evts_in_half_window, 0]-out_features[i, j, 0]

    # normalize
    # Get min, max value aming all elements for each column
    x_min = np.min(out_features, axis=tuple(
        range(out_features.ndim-1)), keepdims=1)
    x_max = np.max(out_features, axis=tuple(
        range(out_features.ndim-1)), keepdims=1)

    # Normalize with those min, max values leveraging broadcasting
    out_features = (out_features - x_min) / (x_max - x_min)

    out_results = np.resize(
        out_results, (out_results.shape[0], out_results.shape[2]))

    time_end = time.time()

    print("--- load from file     :  %s seconds ---" %
          (time_process-time_start))
    print("--- data manipulations :  %s seconds ---" % (time_end-time_process))

    return out_features, out_results
