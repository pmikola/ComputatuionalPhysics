# 4.5 Spontaneous Decay (Implementation and Visualisation)

import random
import winsound
import matplotlib.pyplot as plt
import numpy as np


def SpontanDec(time_max, number, nloop, lambda1):
    x = []
    y = []
    for time in np.arange(0, time_max + 1):
        for _ in np.arange(1, number + 1):
            decay = random.random()
            if decay < lambda1:
                nloop -= 1
                # winsound.Beep(random.randint(600, 700), 20)  # Beep at rand Hz for 100 ms
        number = nloop
        x.append(time)
        y.append(abs(number))
    plt.plot(x, y, '-')
    plt.yscale("log")
    plt.grid(True)
    plt.show()


# 1 Plot the logarithm of the number left ln N(t) and the logarithm of the decay
# rate ln ΔN(t)∕Δt(= 1) vs. time. Note that the simulation measures time in
# steps of Δt (generation number).

lambda1 = 0.0025
max = 100.
time_max = 1000
random.seed(2021)
number = nloop = max

plt.figure(1)
SpontanDec(time_max, number, nloop, lambda1)
plt.xlabel('time')
plt.ylabel('lnN(t)')

# 2 Check that you obtain what looks like the exponential decay when you start
# with large values for N(0), but that the decay displays its stochastic nature for
# small N(0). (Large N(0) values are also stochastic; they just do not look like it.)
m = 100
number = number * m
plt.figure(2)
SpontanDec(time_max, number, nloop, lambda1)
plt.xlabel('time')
plt.ylabel('lnN(t)')

# 3 Create two plots, one showing that the slopes of N(t) vs. t are independent
# of N(0) and another showing that the slopes are proportional to the value chosen
# for λ.

number = number * 10 / m
plt.figure(3)
for i in range(0, 15):
    SpontanDec(time_max, number, nloop, lambda1)
    plt.xlabel('time')
    plt.ylabel('lnN(t)')
    lambda1 += 0.0025

# 4 Create a plot showing that within the expected statistical variations, ln N(t)
# and ln ΔN(t) are proportional.

# 5 Explain in your own words how a process that is spontaneous and random at
# its very heart can lead to the exponential decay.

# 6 How does your simulation show that the decay is exponential-like and not a
# power law such as N = βt−α?