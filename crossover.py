import numpy as np


def crossover(pop, pc):
    px, py = pop.shape
    newpop = np.ones_like(pop)
    for i in np.arange(0, px, 2):
        if (np.random.rand() < pc):
            cpoint = int(np.round(np.random.rand() * py)) - 1
            newpop[i, :] = np.concatenate(
                (pop[i, 0:cpoint], pop[i+1, cpoint:py]))
            newpop[i+1,
                   :] = np.concatenate((pop[i+1, 0:cpoint], pop[i, cpoint:py]))
        else:
            newpop[i, :] = pop[i, :]
            newpop[i+1, :] = pop[i+1, :]
    return newpop


if __name__ == "__main__":
    pop = np.array([[0, 0, 0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]])
    pc = 0.6
    crossover(pop, pc)
