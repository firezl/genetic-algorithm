import numpy as np


def mutation(pop, pm):
    px, py = pop.shape
    newpop = np.ones_like(pop)
    for i in range(0, px):
        if np.random.rand() < pm:
            mpoint = np.round(np.random.rand()*py)
            if mpoint <= 0:
                mpoint = 1
            newpop[i, :] = pop[i, :]
            if newpop[i, mpoint] == 0:
                newpop[i, mpoint] = 1
            else:
                newpop[i, mpoint] = 0
        else:
            newpop[i, :] = pop[i, :]
    return newpop
