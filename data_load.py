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

    print(datum[0].shape)
    print(labels[0].shape)


data_by_month(5, 7, 3, False)