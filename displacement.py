import numpy as np
import math
from numpy.random import rand
from numpy import random

a = np.zeros((100, 2), dtype=np.float)


# Single random walk
def randwalk(x, y):  # Defines the randwalk function
    theta = 2 * math.pi * rand()
    x += math.cos(theta)
    y += math.sin(theta)
    return (x, y)  # Function returns new (x,y) coordinates


x, y = 0., 0.  # Starting point is the origin
for i in range(100):  # Walk contains 1000 steps
    x, y = randwalk(x, y)
    a[i, :] = x, y  # Replaces entries of a with (x,y) coordinates

# Repeating random walk 12 times
fn_base = "random_walk_%i.txt"  # Saves each run to sequentially named .txt
for j in range(1):
    random.seed(None)
    x, y = 0., 0.
    for i in range(100):
        x, y = randwalk(x, y)
        a[i, :] = x, y
    fn = fn_base % j  # Allocates fn to the numbered file
    np.savetxt(fn, a)


def compute_MSD(path):
    totalsize = len(path)
    msd = []
    for i in range(totalsize - 1):
        j = i + 1
        msd.append(np.sum((path[0:-j] - path[j::]) ** 2) / float(totalsize - j))

    msd = np.array(msd)
    return msd
