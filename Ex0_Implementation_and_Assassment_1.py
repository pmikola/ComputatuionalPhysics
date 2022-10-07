from numpy import *
from math import *
import matplotlib.pyplot as plt


# term_factorial1 = (((-1)**(n-1))*(x**(2*n-1))) / factorial((2*n-1))
# term_factorial2 = (((-1)**(n-2))*(x**(2*n-3))) / factorial((2*n-3))
# term_diff = -x**2 / ((2*n-1)*(2*n-2))
def sumSinx(x, n, eps, display, identity):
    if identity == 1:
        div = x / pi
        div = int(div)
        if div % 2 == 0:
            x = math.fmod(x, 1 * pi)
        else:
            x = -math.fmod(x, 1 * pi)
    else:
        pass
    names = ["x", "sum", "-sum", "sin(x)", "relative error"]
    table = [names]
    term = x
    sum = x
    i = 0
    error_series = []
    error = 1.
    N = []
    while abs(term / sum) > eps:
        # print(abs(term / sum)) # eps per iter
        N.append(n)
        error = abs(term / sum)
        error_series.append(abs(term / sum))
        sum_prev = sum
        term *= ((-1 * x ** 2) / (2 * n - 1) / (2 * n - 2))
        sum = sum + term
        sum = float("{:.20f}".format(sum))
        tab_values = [x, sum, -sum, float("{:.20f}".format(sin(x))), abs(sum - sum_prev)]
        table.append(tab_values)
        n += 1
        i += 1
    if display == 1:
        plt.plot(i, table[i][2], "-o")
    elif display == 2:
        len_table = len(table)
        for i in range(len_table):
            print(table[i])
        print("convValue = ", f'{table[-1][1]:.20f}')
        print("sin(x) = ", '%.20f' % sin(x))
        print("Conv Precision =>", f'{abs(table[-1][1] - sin(x)):.20f}')
    else:
        pass
    result = [table[-1][1], error, N, error_series]
    return result


display = 2
SinCovValue = []
SinusTrueValue = []
Start = 1E-15
Stop = 3 * pi
Step = 0.1
n = 2.
eps = 1E-18

# Summation function for sin(x)
for i in arange(Start, Stop, Step):
    Sinus, error, error_series,N = sumSinx(i, n, eps, display, 0)
    SinCovValue.append(Sinus)
    SinusTrueValue.append(sin(i))
if display == 3:
    print(SinCovValue)
plt.plot(arange(Start, Stop, Step), SinCovValue, '-ro')
plt.plot(arange(Start, Stop, Step), SinusTrueValue, '-k')
plt.grid()
plt.show()
