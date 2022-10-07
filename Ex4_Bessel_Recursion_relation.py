# Bessel up and down recursive algoruthm
# - substractive cancelation in up numerical
# implementation bacause of nonideality of hardwate
# get really big errors after time
from pandas import *
from numpy import *
from matplotlib.pyplot import *

Xmax = 10.
Xmin = 0.1
step = 0.01
start = 100


def down(x, n, m):
    # good alg - algorithm converge and is stable, approximation to 10-9 achived
    j = zeros((start + 2))
    j[m + 1] = j[m] = 1.
    for k in arange(m, 0, -1):
        j[k - 1] = ((2. * k + 1.) / x) * j[k] - j[k + 1]
    scale = (sin(x) / x) / j[0]
    return j[n] * scale


def up(x, n, m):
    # bad alg - algorithm converge but are not
    # stable at the beginning (big approx error)
    # Valid only for first Bessel mode
    j = zeros((start + 2))
    j[m + 1] = j[m - start + 1] = j[m - start] = 1.
    scale = (sin(x) / x) / j[0]
    for k in arange(m - start, start, 1):
        j[k + 1] = ((2. * k + 1.) / x) * j[k] - j[k - 1]
    if 1 >= j[n] * scale >= -1:
        return j[n] * scale
    elif j[n] * scale >= -1:
        return -1
    else:
        return 1


ion()
fig, (ax1, ax2) = subplots(2)

x01up = []
x1up = []
x10up = []
x01down = []
x1down = []
x10down = []

flag = 1

for order in arange(0, 2, 1):
    for x in arange(Xmin, Xmax, step):
        if flag == 1:
            ax1.plot(x, down(x, order, start), 'or')
            ax2.plot(x, up(x, order, start), 'og')
        elif flag == 2:
            if x == 0.1:
                x01down.append(down(x, order, start))
                x01up.append(up(x, order, start))
            elif x == 1:
                x1down.append(down(x, order, start))
                x1up.append(up(x, order, start))
            elif x == 10:
                x10down.append(down(x, order, start))
                x10up.append(up(x, order, start))
            else:
                pass
        else:
            print(order, down(x, order, start), up(x, order, start),
                  abs(up(x, order, start) - down(x, order, start)) / (
                              abs(up(x, order, start)) + abs(down(x, order, start))))

ax1.set(xlabel="x", ylabel="jl(x)")
ax1.grid(True, which="both")
ax2.set(xlabel="x", ylabel="jl(x)")
ax2.grid(True, which="both")

fig.tight_layout(pad=1.0)
pause(20)
show()
close(fig)
Frame = DataFrame({"xup = 01": array(x01up), "xup = 1": array(x1up), "xup = 10": array(x10up), \
                   "xdown = 01": array(x01down), "xdown = 1": array(x1down), "xdown = 10": array(x10down)})
print(Frame)
