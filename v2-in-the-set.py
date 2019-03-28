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
    if np.linalg.norm(z) > 2:
        return False
    else:
        return True


#tests
print(mandle([1, 1]))
print(mandle([-1, 0]))
print(mandle([0.2, 0.25]))
