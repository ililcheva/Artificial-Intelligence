import numpy as np
# import random
from GAmethods import Evaluate, select_parent, crossover, mutate

# iterator
t = 0

# number of epochs
epochs = 50

# initialize algorithm parameters
n = 10
k = 10
m = 5
LR = 0.5

# initialize probability vector P[i] 
P = np.zeros(n)
P[0:n] = 0.5 



# start genetic algorithm
while t < epochs:
    solution_vectors = [dict({"gene": [], "fitness": 0}) for x in range(k)]
    for j in range(0, k):
        for i in range(0,n):
            # generate population based on the probablistic vector
            if np.random.random_sample() <= P[i]:
                solution_vectors[j]["gene"].append(1)
            else:
                solution_vectors[j]["gene"].append(0)
        solution_vectors[j]["fitness"] = Evaluate(solution_vectors[j])
    
    # initialize next generation
    generation = []

    for ind in range(0, k):
        # select parents from the generated population
        # which is the solution_vector computed above
        ind1 = select_parent(solution_vectors)
        ind2 = select_parent(solution_vectors)

        # retrieve 2 children from the crossover algorithm
        ch1, ch2 = crossover(ind1, ind2)

        # mutate genes of the children separately
        ch1 = mutate(ch1)
        ch2 = mutate(ch2)

        #evaluate children
        ch1["fitness"], ch2["fitness"] = Evaluate(ch1), Evaluate(ch2)
        
        # store children in current generation
        generation.append(ch1)
        generation.append(ch2)
        
     # update the solution vectors to be the current generation
    solution_vectors = generation

    # sort the current generation by fitness in descending order
    solution_vectors = sorted(solution_vectors, key=lambda k: k['fitness'],reverse=True) 

    # update probablistic vector P[i] using the current generation
    for j in range(0,m):
        for i in range(0,n):
            P[i] = P[i] * (1 - LR) + solution_vectors[j]["gene"][i]*(LR)
    
    print('Iteration {0}: {1}'.format(t, P))
    # update iterator
    t += 1

