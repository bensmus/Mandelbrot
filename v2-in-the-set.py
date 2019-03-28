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


def graphpoints(points):
    x = np.array([])
    y = np.array([])

    for point in points:
        x = np.append(x, point[0])
        y = np.append(y, point[1])

    plt.scatter(x, y, s = 1)
    plt.show()


points = []
for x in np.arange(-2, 2, 0.01):
    for y in np.arange(-2, 2, 0.01):
        points.append(np.array([x, y]))


pointsmandle = [point for point in points if mandle(point) == True]

# graph these points!
graphpoints(pointsmandle)
