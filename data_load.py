import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xarray as xa
import pandas as pd
import random

from control.config import args
import cftime

from util.graph_adjacencies import temporal_graph
from data_process import return_data
from dataset.datasets import *

from torch.utils.data import DataLoader

def data_by_month(lead_months, window, target_month, use_heat_content):
    datum, labels = return_data(lead_months, window, target_month, use_heat_content)
    dataset, dataset_test = [], []

    for i in range(datum[1].shape[0]):
        dataset.append((datum[1][i,0,:,:,:], labels[1][i]))
    for i in range(datum[2].shape[0]):
        dataset.append((datum[2][i,0,:,:,:], labels[2][i]))
    for i in range(datum[0].shape[0]):
        dataset_test.append((datum[0][i,0,:,:,:], labels[0][i]))

    return dataset, dataset_test

def data_total(lead_months, window, use_heat_content):
    dataset, dataset_test = [], []

    for target_month in range(1, 13):

        datum, labels = return_data(lead_months, window, target_month, use_heat_content)

        for i in range(datum[1].shape[0]):
            dataset.append((datum[1][i,0,:,:,:], labels[1][i]))
        for i in range(datum[2].shape[0]):
            dataset.append((datum[2][i,0,:,:,:], labels[2][i]))
        for i in range(datum[0].shape[0]):
            dataset_test.append((datum[0][i,0,:,:,:], labels[0][i]))
    
    return dataset, dataset_test

def get_dataloaders():
    train, test = data_by_month(3, 5, 1, False)
    random.shuffle(train)

    train_data = train[:int(0.8 * len(train))]
    validation_data = train[int(0.8 * len(train)):]

    train_dataset = single_feature_Dataset(args, train_data, "Training Dataset")
    validation_dataset = single_feature_Dataset(args, validation_data, "Validation Dataset")
    test_dataset = single_feature_Dataset(args, test, "Test Dataset")

    train_loader = DataLoader(train_dataset, batch_size=args.batch_size, drop_last=True)
    validation_loader = DataLoader(validation_dataset, batch_size=args.batch_size, drop_last=True)
    test_loader = DataLoader(test_dataset, batch_size=args.batch_size, drop_last=True)

    return train_loader, validation_loader, test_loader