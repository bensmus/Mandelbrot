import numpy as np
import matplotlib.pyplot as plt

def zAdd(z1, z2):
    '''vector addition'''
    x1 = z1[0]
    y1 = z1[1]
    x2 = z2[0]
    y2 = z2[1]
    return [x1 + x2, y1 + y2]

def zSquared(z):
    '''complex squaring, interpreting
    x, y as the real and complex parts
    formula derived from (a+bi)(a+bi)'''
    x = z[0]
    y = z[1]
    return [x**2 - y**2, 2*x*y]

def mandleFunc(c):
    '''z(c) = z^2 + c, where c is the initial
    complex number'''
    z = zAdd(zSquared(c), c)
    return z

c = [1, 0]
z = mandleFunc(c)
print(z)
'''
plt.plot(x, y)
plt.show()
'''
