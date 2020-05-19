import numpy as np
import json
from util import write_json


###############################################################################
params = {
    "problem": "TSP",
    "N": 11
}
###############################################################################


def generate_data(params):
    lats = np.random.uniform(low=-90.0, high=90.0, size=params["N"])
    longs = np.random.uniform(low=-180.0, high=180.0, size=params["N"])
    nodes = [(i,x,y) for (i,x,y) in zip(range(1, params["N"]+1), lats, longs)]

    data = {
        "filename": params["problem"] + "_" + str(params["N"]) + ".json",
        "N": params["N"],
        "nodes": nodes,
        "solutions": {}
    }

    return data


if __name__ == "__main__":
    write_json(generate_data(params))