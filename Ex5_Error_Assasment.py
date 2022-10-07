from Ex0_Implementation_and_Assassment_1 import sumSinx
from numpy import *
import matplotlib.pyplot as plt

display = 3
finalResult = []
n = 2.
Start = 0.01
Stop = 20.
Step = 1.
eps = 1E-7
# 0.00000000004066291748 n~= x /2 for eps = 1E-7
# algorithm converge for x < 37 without identity sin(x +2pi) = sin(x)

# Taylor series algorithm for sin(x)
for i in arange(Start, Stop, Step):
    result = sumSinx(i, n, eps, display, 0)
    # finalResult.append(result[1])
    plt.semilogy(result[2], result[3])  # Convergence graph

# plt.semilogy(arange(Start, Stop, Step), array(finalResult), '-o')

plt.yscale('symlog')
plt.xlabel('Number of terms in series')
plt.ylabel('Error')
plt.grid(True, which="both")
plt.show()
