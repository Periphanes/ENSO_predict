import os
import random

import torch

import pickle
from tqdm import tqdm

class single_feature_Dataset(torch.utils.data.Dataset):
    def __init__(self, args, data, data_type="dataset"):
        self._data_list = data
    
    def __len__(self):
        return len(self._data_list)
    
    def __getitem__(self, index):
        return self._data_list[index]