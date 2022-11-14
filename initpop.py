import numpy as np


def initpop(popsize, chromlength):
    pop = np.round(np.random.rand(popsize, chromlength))
    return pop
