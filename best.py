def best(pop, fitvalue):
    px, py = pop.shape
    bestindividual = pop[1, :]
    bestfit = fitvalue[1]
    for i in range(0, px):
        if fitvalue[i] > bestfit:
            bestindividual = pop[i, :]
            bestfit = fitvalue[i]

    return bestindividual, bestfit
