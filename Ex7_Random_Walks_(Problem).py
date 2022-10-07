from numpy import random
from matplotlib import pyplot as plt
from math import *


# 4,3 Random Walks (Problem)
# 4.3.1 Random-Walk Simulation

def div_zero_exept(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0


def power(my_list, power):
    return [x ** power for x in my_list]


def divide(my_list, div):
    return [x * (1 / div) for x in my_list]


def sqr(my_list):
    return [sqrt(x) for x in my_list]


def abs_list(my_list):
    return [abs(x) for x in my_list]


num_of_trials = 10

R_trials = []

for k in range(0, num_of_trials):
    random.seed()
    imax = 200
    jmax = 200
    x, y = [], []
    x.append(0)
    y.append(0)
    delta_x = 0
    delta_y = 0
    R = []
    walk = plt.figure(1)

    for j in range(0, jmax):
        for i in range(0, imax + 1):
            x.append(delta_x)
            y.append(delta_y)
            delta_x += ((random.random() - 0.5) * 2)  # -1 <= x <= 1
            delta_y += ((random.random() - 0.5) * 2)  # -1 <= y <= 1
            # L = sqrt(pow(delta_x, 2) + pow(delta_y, 2))
            # delta_x = (1 / L) * delta_x
            # delta_y = (1 / L) * delta_y
        R.append((sum(abs_list(x)) + sum(abs_list(y))) / (len(x) + len(y)))
        plt.plot(x[:], y[:], '-r')
        x, y = [], []

    N = [*range(0, imax)]
    plt.grid()
    walk.show()

    Rmsd = plt.figure(2)
    plt.plot(R)
    plt.plot([*range(0, len(R))])
    plt.grid()
    Rmsd.show()
    R_trials.append(sum(R))

allTrials = plt.figure(3)
plt.plot(R_trials)
plt.grid()
allTrials.show()

