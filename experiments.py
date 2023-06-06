import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xarray as xa
import pandas as pd

from control.config import args
import cftime

godas_data = 'data/GODAS/GODAS.input.36mn.1980_2015.nc'
godas_label = 'data/GODAS/GODAS.label.12mn_3mv.1982_2017.nc'
soda_data = 'data/SODA/SODA.input.36mn.1871_1970.nc'
soda_label = 'data/SODA/SODA.label.nino34.12mn_3mv.1873_1972.nc'
cmip5_data = 'data/CMIP5/CMIP5.input.36mn.1861_2001.nc'
cmip5_label = 'data/CMIP5/CMIP5.label.nino34.12mn_3mv.1863_2003.nc'

gd = xa.open_dataset(godas_data)
gl = xa.open_dataset(godas_label)
sd = xa.open_dataset(soda_data)
sl = xa.open_dataset(soda_label)
cd = xa.open_dataset(cmip5_data, decode_times=False)
cl = xa.open_dataset(cmip5_label, decode_times=False)

data = [gd, sd, cd]
labels = [gl, sl, cl]

