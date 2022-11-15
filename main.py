import numpy as np
import matplotlib.pyplot as plt

from best import best
from binary2decimal import binary2decimal
from cal_objvalue import cal_objvalue
from crossover import crossover
from initpop import initpop
from mutation import mutation
from selection import selection

popsize = 1000
chromlength = 10
pc = 0.6
pm = 0.01
pop = initpop(popsize, chromlength)
print(pop)
for i in range(0, 500):
    objvalue = cal_objvalue(pop)
    fitvalue = objvalue
    newpop = selection(pop, fitvalue)
    newpop = crossover(newpop, pc)
    newpop = mutation(newpop, pm)
    pop = newpop
    bestindividual, bestfit = best(pop, fitvalue)
    x2 = binary2decimal(bestindividual)
    x1 = binary2decimal(newpop)
    y1 = cal_objvalue(newpop)
    if (i+1) % 500 == 0:
        x = np.linspace(0, 10, 100)
        y = 10 * np.sin(5 * x) + 7 * np.abs(x - 5) + 10
        fig = plt.figure()
        plt.plot(x, y, '-b')
        plt.plot([x2]*popsize, y1, '*r')
        plt.plot(x1, y1, "*b")
        plt.title("迭代次数为n=%s" % str(i))
        plt.show()

print("The best X is --->> %5.2f" % x2)
print("The best Y is --->> %5.2f" % bestfit)
