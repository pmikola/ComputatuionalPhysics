#diffrent summation analitical expression - substractive cancelation
from numpy import *
from matplotlib.pyplot import *
from decimal import *
getcontext().prec = 10

S1 = lambda n: ((-1)**n)*n/(n+1)
S2 = lambda n: -((2*n-1)/(2*n)) + (2*n)/(2*n+1)
S3 = lambda n: 1/(2*n*(2*n+1))

Sup = lambda n: 1 / n
Sdown = lambda n: 1 / n

S1_Solution = []
S2_Solution = []
S3_Solution = []
Sup_Solution = []
Sdown_Solution = []
NoPoint = []
difference = []
Start = 1.
Stop = 1.E+3
Step = 1.
for n in arange(Start, Stop,Step):
    S1_Solution.append(float("{:.20f}".format(S1(n))))
    S2_Solution.append(float("{:.20f}".format(S2(n))))
    S3_Solution.append(float("{:.20f}".format(S3(n))))
    Sup_Solution.append(float("{:.20f}".format(Sup(n))))
    Sdown_Solution.append(float("{:.20f}".format(Sdown(Stop - n))))
    NoPoint.append(n)


S1_array = array(S1_Solution)
S2_array = array(S2_Solution)
S3_array = array(S3_Solution)
Sup_array = array(Sup_Solution)
Sdown_array = array(Sdown_Solution)

Subtraction1 = subtract(S1_array, S3_array)
RelativeError1 = divide(Subtraction1, S2_array)

Subtraction2 = subtract(Sup_array,Sdown_array)
RelativeError2 = divide(Subtraction2,(add(abs(Sup_array),abs(Sdown_array))))

fig, ((ax1, ax2), (ax3, ax4)) = subplots(2,2)
ax1.loglog(NoPoint, abs(RelativeError1), label="err")
ax2.loglog(NoPoint, RelativeError2,'--', label="err")
ax3.semilogy(NoPoint,Sup_array)
ax4.semilogy(NoPoint,Sdown_array,'--')

ax1.set(xlabel="Number of terms", ylabel="Relative Error")
ax2.set(xlabel="Number of terms", ylabel="Relative Error")
ax3.set(xlabel="Number of terms", ylabel="SupValue")
ax4.set(xlabel="Number of terms", ylabel="SdownValue")

ax1.grid(True, which="both")
ax2.grid(True, which="both")
ax3.grid(True, which="both")
ax4.grid(True, which="both")

ax1.legend()
ax2.legend()

fig.tight_layout(pad=1.0)
draw()
pause(100)
close(fig)
#print(sum(S1_Solution)) ; print(sum(S2_Solution))  ; print(sum(S3_Solution))

#Error is proportional to power of N
#Sdown is more precise than
# Sup because with summing time
# we get bigger error iterating
# from 1 to n and smaller from n to 1.
# Thats because we start in the Sup from
# the one and add more and more fractions
# with more errors, and in Sdown the opposite
# with is less prone to rounding error
# (and biger rounding error is at the beggining)
