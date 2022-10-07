# P1
# Quadratic equation & substractive cancelation Ex2_1.
# ax^2 + bx + c = 0
from numpy import *
from cmath import sqrt
from matplotlib.pyplot import *

def QuadraticEq(a, b, c):
    # solutions
    x1 = (- b + sqrt(b ** 2 - 4 * a * c)) / 2 * a
    x2 = (- b - sqrt(b ** 2 - 4 * a * c)) / 2 * a

    x1_prim = (- 2 * c) / (b + sqrt(b ** 2 - 4 * a * c))
    x2_prim = (- 2 * c) / (b - sqrt(b ** 2 - 4 * a * c))

    return x1, x2, x1_prim, x2_prim

i = 10.
j = 1.
x1_solution = [] ; x2_solution = [] ; x1_prim_solution = []
x2_prim_solution = [] ; x1_minus_x2 = [] ; x1_prim_minus_x2_prim = []
points = []
boundry = 1.
for k in arange(-50, 50., 0.1):
    c = pow(10, -k)
    x1, x2, x1_prim, x2_prim = QuadraticEq(i, j, c)
    if (j**2)/20 >= 4*i*c:
        if boundry == 0:
            boundry = k
        else:
            pass
    else:
        boundry = 0
    x1_solution.append(x1)
    x2_solution.append(x2)
    x1_prim_solution.append(x1_prim)
    x2_prim_solution.append(x2_prim)

    print(x1, x2, x1_prim, x2_prim)
    print(k)
    print(c)
    points.append(k)

    x1_minus_x2.append(-x1 + x2)
    x1_prim_minus_x2_prim.append(-x1_prim + x2_prim)

arr = [abs(x1_solution[-1]),abs(x2_solution[-1]),abs(x1_prim_solution[-1]),abs(x2_prim_solution[-1])]
arr_name = ["x1","x2","x1_prim","x2_prim"]

k = 1E-100
x_array_values = sorted(array(arr).real)
print(x_array_values)
min_value = min(i for i in x_array_values if i > k)

print("most precision solution is",str(min_value))
ion()
fig = figure()

x1_minus_x2_percent = -1*array(x1_minus_x2)*100
x1_prim_minus_x2_prim_percent = -1*array(x1_prim_minus_x2_prim)*100
flag = 0
if flag == 1:
    xlabel('No. Points [n]')
    ylabel('error [%]')
    plot(points,x1_minus_x2_percent, "-o",label='x1_minus_x2')
    plot(points,x1_prim_minus_x2_prim_percent, "-r",label='x1_prim_minus_x2_prim')
else:
    xlabel('No. Points [n]')
    ylabel('Quadratic values of x')
    plot(points,x1_solution, label='x1')
    plot(points,x2_solution,label='x2')
    plot(points,x1_prim_solution,label='x1_prim')
    plot(points,x2_prim_solution,label='x2_prim')



if boundry != 0:
    axvline(boundry, color="purple",ls='--')
else:
    pass
grid()
legend()
draw()
pause(5)
#input("Press [enter] to continue.")
close(fig)
#show()
# fig.canvas.draw()
# fig.canvas.flush_events()

