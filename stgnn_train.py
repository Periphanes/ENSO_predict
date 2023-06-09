import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

import seaborn as sns
import math
import random
import os

from control.config import args
from data_load import get_dataloaders

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
args.seed = 1004

torch.manual_seed(args.seed)
torch.cuda.manual_seed_all(args.seed)
np.random.seed(args.seed)
random.seed(args.seed)

torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False

if args.cpu or not torch.cuda.is_available():
    device = torch.device('cpu')
else:
    device = torch.device('cuda')

print("Device Used : ", device)
args.device = device

train_loader, val_loader, test_loader = get_dataloaders()
