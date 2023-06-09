import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xarray as xa
import pandas as pd

from control.config import args
import cftime

from util.graph_adjacencies import temporal_graph
from data_process import return_data

def data_by_month(lead_months, window, target_month, use_heat_content):
    datum, labels = return_data(lead_months, window, target_month, use_heat_content)

    X,y = [], []

    for i in range(datum[1].shape[0]):
        X.append(datum[1][i,0,:,:,:])
        y.append(labels[1][i])
    for i in range(datum[2].shape[0]):
        X.append(datum[2][i,0,:,:,:])
        y.append(labels[2][i])

    X_test, y_test = [], []

    for i in range(datum[0].shape[0]):
        X_test.append(datum[0][i,0,:,:,:])
        y_test.append(labels[0][i])

    return X, y, X_test, y_test

def data_total(lead_months, window, use_heat_content):

    X,y = [], []
    X_test, y_test = [], []

    for target_month in range(1, 13):

        datum, labels = return_data(lead_months, window, target_month, use_heat_content)

        for i in range(datum[1].shape[0]):
            X.append(datum[1][i,0,:,:,:])
            y.append(labels[1][i])
        for i in range(datum[2].shape[0]):
            X.append(datum[2][i,0,:,:,:])
            y.append(labels[2][i])

        for i in range(datum[0].shape[0]):
            X_test.append(datum[0][i,0,:,:,:])
            y_test.append(labels[0][i])
    
    return X, y, X_test, y_test
        

data_by_month(5, 7, 3, False)