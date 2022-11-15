def best(pop, fitvalue):
    px, py = pop.shape
    bestindividual = pop[0, :]
    bestfit = fitvalue[0]
    for i in range(0, px):
        if fitvalue[i] > bestfit:
            bestindividual = pop[i, :]
            bestfit = fitvalue[i]

    return bestindividual.reshape(1, py), bestfit
