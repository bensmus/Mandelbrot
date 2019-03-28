import numpy as np
import matplotlib.pyplot as plt

def square(z):
    x = z[0]
    y = z[1]
    return np.array([x**2 - y**2, 2*x*y])


def mandle(c, itercount = 10):
    z = c
    for i in range(itercount):
        z = square(z) + c
        print(z)

'''tests
mandle([-1, 0])
mandle([-0.5, 0])
mandle([0, 0.5])
mandle([0.2, 0.25])
'''
