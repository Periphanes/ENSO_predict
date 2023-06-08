import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--dir-result', type=str, default='.')
parser.add_argument('--project-name', type=str, default='proj')
parser.add_argument('--seed-list', type=list, default=[5, 23, 7, 89, 4])
parser.add_argument('--cpu', type=bool, default=False)

parser.add_argument('--input-types', type=str, default="static", choices=["static", "txt", "audio", "sig", "audio_txt", "audio_txt_shortform", "txt_shortform", "audio_shortform"])
parser.add_argument('--model', type=str, default="default_model")

parser.add_argument('--epochs', type=int, default=100)
parser.add_argument('--batch-size', type=int, default=16)

parser.add_argument('--use-heat-content', type=bool, default=False)
# k-hop neighborhood for the initial adjacency graphs before neural sparsification
parser.add_argument('--adj-neighborhood', type=int, default=3)

args = parser.parse_args()
args.dir_root = os.getcwd()

args.godas_data = 'data/GODAS/GODAS.input.36mn.1980_2015.nc'
args.godas_label = 'data/GODAS/GODAS.label.12mn_3mv.1982_2017.nc'
args.soda_data = 'data/SODA/SODA.input.36mn.1871_1970.nc'
args.soda_label = 'data/SODA/SODA.label.nino34.12mn_3mv.1873_1972.nc'
args.cmip5_data = 'data/CMIP5/CMIP5.input.36mn.1861_2001.nc'
args.cmip5_label = 'data/CMIP5/CMIP5.label.nino34.12mn_3mv.1863_2003.nc'