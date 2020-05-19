import numpy as np
import json
import sys
import time
import itertools as it
from util import read_json, write_json, tsp_fitness, build_distance_matrix


def tsp_brute_force(filename):
    print("{:.4f} s | Reading file...".format(time.perf_counter()-before))
    data = read_json(filename)
    data["optimal"] = False

    print("{:.4f} s | Building distance matrix...".format(time.perf_counter()-before))
    d = build_distance_matrix(data["nodes"])
    base = {"sequence": [i for i in range(data["N"])], "fitness": tsp_fitness([i for i in range(data["N"])], d)}
    
    best_solution = {"sequence": base["sequence"], "fitness": base["fitness"], "gap": 1, "type": "exact"}

    for incoming in it.permutations(base["sequence"]):
        incoming_fitness = tsp_fitness(incoming, d)
        if incoming_fitness < best_solution["fitness"]:
            best_solution["sequence"] = incoming
            best_solution["fitness"] = incoming_fitness
            best_solution["gap"] = incoming_fitness/base["fitness"]
            print("{:.4f} s | sequence: {} | fitness: {} | gap: {:.4f}%".format(time.perf_counter()-before, incoming, incoming_fitness, best_solution["gap"]*100))

            best_solution["best_time"] = (time.perf_counter() - before)/60
            best_solution["total_time"] = (time.perf_counter() - before)/60
            data["solutions"]["brute_force"] = best_solution
            #write_json(data)
        
        #else:
        #    best_solution["total_time"] = (time.perf_counter() - before)/60
        #    write_json(data)

    data["optimal"] = True
    write_json(data)
    print("Solved with exact solution!")

    return best_solution


if __name__ == "__main__":
    filename = sys.argv[1]
    before = time.perf_counter()
    tsp_brute_force(filename)

    
    