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

gd = xa.open_dataset(godas_data, decode_times=False)
gl = xa.open_dataset(godas_label, decode_times=False)
sd = xa.open_dataset(soda_data, decode_times=False)
sl = xa.open_dataset(soda_label, decode_times=False)
cd = xa.open_dataset(cmip5_data, decode_times=False)
cl = xa.open_dataset(cmip5_label, decode_times=False)


args.lon_min = 0
args.lon_max = 360
args.lat_min = -55
args.lat_max = 60

def data_retrieve(lead_months=3, window=3, use_heat_content=False, 
                  lon_min=args.lon_min, lon_max=args.lon_max, 
                  lat_min=args.lat_min, lat_max=args.lat_max, 
                  data=gd, label=gl, mixed_months=False, 
                  target_month=5, data_type="CMIP5", return_labels=False):
    lat_p1, lat_p2 = int((lat_min+55)/5), min(int((lat_max+55)/5),23)
    lon_p1, lon_p2 = int(lon_min/5), min(int(lon_max/5),71)

    lat_sz = lat_p2 - lat_p1 + 1
    lon_sz = lon_p2 - lon_p1 + 1
    features = 2 if use_heat_content else 1
    feature_names = ["sst", "heat_content" if use_heat_content else ["sst"]]

    filtered_region = data.sel(
        {'lat':slice(lat_min, lat_max), 'lon':slice(lon_min, lon_max)}
    )
    filtered_region = filtered_region.rename({"lev": "window", "time":"year"})

    # if mixed_months == False:
    #     X_early = np.empty((data.sizes["time"], features, window, lat_sz, lon_sz))
    #     y_early = np.empty((data.sizes["time"]))
    # else:
    #     X_early = np.empty((data.sizes["time"]*12, features, window, lat_sz, lon_sz))
    #     y_early = np.empty((data.sizes["time"]*12))
    
    time = (label.get_index("time") / (24 * 365)).astype(int)
    
    '''
    GODAS Data : Labels from 1982 ~ 2017
    CMIP5 Data : Labels from 1863 ~~
    SODA Data : Labels from 1873 ~ 1972
    '''
    
    if data_type == "CMIP5":
        time = time + 1871
    elif data_type == "GODAS":
        time = time + 1982
    elif data_type == "SODA":
        time = time + 1873

    lat_labels = filtered_region.get_index('lat')
    lon_labels = filtered_region.get_index('lon')

    labels = (time, lat_labels, lon_labels)

    if mixed_months == False:
        window_end = int(25 - lead_months + target_month) + 1
        window_start = int(25 - lead_months + target_month) + 1 - window

        sst_vars = filtered_region.variables["sst"][:, window_start:window_end, :, :].to_numpy()
        sst_vars = np.expand_dims(sst_vars, 1)

        X = sst_vars

        if use_heat_content:
            heat_vars = filtered_region.variables["t300"][:, window_start:window_end, :, :].to_numpy()
            heat_vars = np.expand_dims(heat_vars, 1)

            X = np.concatenate((sst_vars, heat_vars), 1)
    
    y = label.variables["pr"][:, target_month, 0, 0].to_numpy()

    print(y.shape)
    

    '''
    X = (Time, Variables, Window, Latitude, Longitude)
    y = (Time)
    '''

    '''
    TODO : DELETE Terrestrial Nodes
    '''

    # if return_labels:
    #     return X_early, y_early, labels
    # return X_early, y_early


data_retrieve(data_type="GODAS")