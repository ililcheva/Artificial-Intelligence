''' Just some implementations of the methods to test the algorithm '''

import numpy as np
import random

def Evaluate(parent):
    # calculates fitness based on # of 1s
    return sum([gene for gene in parent["gene"] if gene == 1])

def select_parent(population):
    fitness_sum = sum([ind["fitness"] for ind in population])
    
    probability_offset = 0

    for ind in population:
        ind["probability"] = probability_offset + (ind["fitness"] / fitness_sum)
        probability_offset += ind["probability"]

    selected_ind = population[0] 
    for ind in population:
        if ind["probability"] > np.random.random_sample():
            break; 
        selected_ind = ind
        
    return selected_ind

def crossover(ind1, ind2):
    crossover_point = int(random.randint(1, len(ind1) - 1))
    ind1["gene"][crossover_point:], ind2["gene"][crossover_point:] = ind2["gene"][crossover_point:], ind1["gene"][crossover_point:]
    return ind1, ind2   

def mutate(ind):
    for bit in range(0, len(ind["gene"])):
        if np.random.random_sample() <= 0.005: # mutation rate
            ind["gene"][bit] = 1 - ind["gene"][bit]
    return ind

