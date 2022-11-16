import numpy as np


def mutation(pop, pm):
    px, py = pop.shape
    newpop = np.ones_like(pop)
    for i in range(0, px):
        if np.random.rand() < pm:
            mpoint = int(np.round(np.random.rand()*py)) - 1
            newpop[i, :] = pop[i, :]
            if newpop[i, mpoint] == 0:
                newpop[i, mpoint] = 1
            elif newpop[i, mpoint] == 1:
                newpop[i, mpoint] = 0
        else:
            newpop[i, :] = pop[i, :]
    return newpop


if __name__ == "__main__":
    pop = np.array([[0, 0, 0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]])
    pm = 0.5
    mutation(pop, pm)
