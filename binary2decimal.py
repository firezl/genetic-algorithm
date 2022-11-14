import numpy as np


def binary2decimal(pop):
    px, py = pop.shape
    pop1 = np.zeros(pop.shape)
    for i in range(0, py):
        pop1[:, i] = 2**(py-i)*pop[:, i]
    temp = np.sum(pop1, 1)
    pop2 = temp*10/1023
    return pop2
