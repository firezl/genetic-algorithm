import numpy as np

from binary2decimal import binary2decimal


def cal_objvalue(pop):
    x = binary2decimal(pop)
    objvalue = 10 * np.sin(5 * x) + 7 * np.abs(x - 5) + 10
    return objvalue
