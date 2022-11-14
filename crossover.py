import numpy as np


def crossover(pop, pc):
    px, py = pop.shape
    newpop = np.ones_like(pop)
    for i in np.arange(0, px-1, 2):
        if (np.random.rand() < pc):
            cpoint = np.round(np.random.rand() * py)
            newpop[i, :] = np.concatenate(
                (pop[i, 0:cpoint], pop[i+1, cpoint:py]))
            newpop[i+1,
                   :] = np.concatenate((pop[i+1, 0:cpoint], pop[i, cpoint:py]))
        else:
            newpop[i, :] = pop[i, :]
            newpop[i+1, :] = newpop[i+1, :]
    return newpop
