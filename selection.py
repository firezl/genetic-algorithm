import numpy as np


def selection(pop, fitvalue):
    px, py = pop.shape
    totalfit = np.sum(fitvalue)
    p_fitvalue = fitvalue/totalfit
    p_fitvalue = np.cumsum(p_fitvalue)
    ms = np.sort(np.random.rand(px))
    fitin = 0
    newin = 0
    newpop = np.ones_like(pop)
    while newin < px:
        if ms[newin] < p_fitvalue[fitin]:
            newpop[newin, :] = pop[fitin, :]
            newin = newin + 1
        else:
            fitin = fitin + 1
    return newpop[:newin]
