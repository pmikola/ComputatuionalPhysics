from matplotlib import pyplot as plt
import numpy as np


# 4.2.2 Implementation: Random Sequences
class MyRandomGen:
    # Linear Congruent Method - random number generator method
    def __init__(self, GenNumb, a, c, M, r_0):
        self.a = a
        self.c = c
        self.M = M
        self.r_0 = r_0
        self.GenNumb = GenNumb
        self.ri = []
        self.xi = []

    def RNG(self):
        self.ri.append(self.r_0)
        for i in range(1, self.GenNumb):
            self.ri.append(((self.a * self.ri[i - 1] + self.c) % self.M))
        self.ri = [x / self.M for x in self.ri]
        return self.ri

    def ScaleRNG(self, A, B):
        for i in range(0, len(self.ri)):
            self.xi.append((A + (B - A)) * self.ri[i])
        return self.xi


# 1. Write a program to generate rng using linear congruent method (4.2)
GenNumb = 10
a = 4
c = 1
M = 9
r_0 = 3

A = 0
B = 1
plt.figure(1)
rng = MyRandomGen(GenNumb, a, c, M, r_0)
rng_seq = rng.RNG()
rng_scaled_seq = rng.ScaleRNG(A, B)
print(rng_seq)

plt.scatter(rng_seq[0:GenNumb - 1], rng_seq[1:GenNumb])
plt.grid()

# 2. For pedagogical purposes, try the unwise choice: (a, c,M, r1) = (57, 1, 256,
# 10). Determine the period, that is, how many numbers are generated before
# the sequence repeats.

# 3. Take the pedagogical sequence of random numbers and look for correlations
# by observing clustering on a plot of successive pairs (xi , yi) = (r2i−1 , r2i ), i =
# 1, 2,…(Do not connect the points with lines.) Youmay “see” correlations (Figure
# 4.1), whichmeans that you should not use this sequence for serious work.

GenNumb = 255  # It takes 255 numgen to get period of repetation pattern
a = 57
c = 1
M = 256
r_0 = 10

rng2 = MyRandomGen(GenNumb, a, c, M, r_0)
rng_seq2 = rng2.RNG()
x_cords = rng_seq2[0:GenNumb - 1]
y_cords = rng_seq2[1:GenNumb]
plt.figure(2)
for x, y in zip(x_cords, y_cords):
    rgb = np.random.rand(3, )
    plt.scatter(x, y, c=[rgb])

plt.grid()

# 4. Make your own version of Figure 4.2; that is, plot ri vs. i.
plt.figure(3)
plt.plot(x_cords, color='green', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='blue', markersize=6)
plt.grid()
plt.xlabel('Sequence Number')
# naming the y axis
plt.ylabel('Random Number')
# giving a title to my graph
plt.title('ri vs i')

# Test the built-in random-number generator on your computer for correlations
# by plotting the same pairs as above. (This should be good for serious work.)
# NUMPY UNIFORM DIST
np.random.seed(1)
R = np.random.uniform(0, 1, GenNumb)
plt.figure(4)
plt.plot(R, color='red', linestyle='dashed', linewidth=3,
         marker='.', markerfacecolor='green', markersize=14)
plt.grid()

q_cords = R[0:GenNumb - 1]
p_cords = R[1:GenNumb]
plt.figure(5)
for q, p in zip(q_cords, p_cords):
    rgb = np.random.rand(3, )
    plt.scatter(q, p, c=[rgb])
plt.grid()

# 6. Test the linear congruent method again with reasonable constants like those
# in (4.11) and (4.12). Compare the scatterplot you obtain with that of the builtin
# random-number generator. (This, too, should be good for serious work.)
GenNumb = 255  # It takes 255 numgen to get period of repetation pattern
a = int("5DEECE66D", 16)
c = int("B", 16)
M = 2 ** 48
r_0 = 1

rng3 = MyRandomGen(GenNumb, a, c, M, r_0)
rng_seq3 = rng3.RNG()
g_cords = rng_seq3[0:GenNumb - 1]
h_cords = rng_seq3[1:GenNumb]
plt.figure(6)
for g, h in zip(g_cords, h_cords):
    rgb = np.random.rand(3, )
    plt.scatter(g, h, c=[rgb])

plt.grid()
