import numpy as np
import json


def haversine(lon1, lat1, lon2, lat2):
 
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
 
    newlon = lon2 - lon1
    newlat = lat2 - lat1
 
    haver_formula = np.sin(newlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(newlon/2.0)**2
 
    dist = 2 * np.arcsin(np.sqrt(haver_formula ))
    km = 6367 * dist #6367 for distance in KM for miles use 3958

    return km


def build_distance_matrix(nodes):
    distance_matrix = np.array([[haversine(x[0], x[1], y[0], y[1]) for x in nodes] for y in nodes])
    distance_matrix = distance_matrix * 6371000/1000

    return distance_matrix


def tsp_fitness(sequence, distance_matrix):
    fitness = 0
    for i in range(len(sequence)-1):
        fitness += distance_matrix[sequence[i-1]][sequence[i]]
    fitness += distance_matrix[sequence[-1]][sequence[0]]

    return fitness


def read_json(filename):
    with open("sample_inputs/" + filename, "r") as file:
        json_data = file.read()
    
    data = json.loads(json_data)

    return data


def write_json(data):
    json_data = json.dumps(data)
    with open("sample_inputs/" + data["filename"], "w") as file:
        file.write(json_data)

    return True