import numpy as np
import torch

from control.config import args

def temporal_graph(datum):
    datum = torch.Tensor(datum)
    datum = datum.permute(1,2,0)

    print("HEY!")
    print(datum.shape)

    adj = np.zeros((datum.shape[0]*datum.shape[1], datum.shape[0]*datum.shape[1]))
    
    for i in range(adj.shape[0]):
        for j in range(adj.shape[1]):
            if i == j:
                continue
            tmp_i_lat = i // datum.shape[1]
            tmp_i_lon = i - datum.shape[1] * tmp_i_lat
            tmp_j_lat = j // datum.shape[1]
            tmp_j_lon = j - datum.shape[1] * tmp_j_lat

            manhatt_dist = abs(tmp_i_lat - tmp_j_lat) + abs(tmp_i_lon - tmp_j_lon)
            if manhatt_dist <= args.adj_neighborhood:
                adj[i][j] = 1
    
    data = datum.view(-1, datum.shape[-1])

    # print(data.shape)
    # print(adj.shape)

    # print(adj)

    return data, adj