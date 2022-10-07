from matplotlib.pyplot import *
#matplotlib.use('TkAgg')
from numpy import *
Xmin = -5; Xmax = 5; Npoints = 500
Delx = (Xmax - Xmin) / Npoints
x1 = arange(Xmin,Xmax,Delx)
x2 = arange(Xmin,Xmax,Delx / 20)

y1 = -sin((x1)*cos(x1*x1))
y2 = exp(-x2/4)*sin(x2)

#Fig1
figure(1)
subplot(2,1,1) # 1st subplot in figure 1
plot(x1,y1,'r',lw=2)
xlabel('x')
ylabel('f(x)')
title('Function y1')
grid(True)
subplot(2,1,2) #2nd subplot in figure 1
plot(x2,y2,'-',lw=2)
xlabel('x')
ylabel('f(x)')
title('Function y2')

#Figure 2

figure(2)
subplot(2,1,1) # 1st subplot in figure 2
plot(x1,y1*y1,'r',lw=2)
xlabel('x'); ylabel('f(x)'); title('Function y1*y2')

# form grid
subplot(2,1,2)
plot(x2,y2*y2,'-',lw=2)
xlabel('x'); ylabel('f(x)'); title('Function y1*y2')
grid(True)
subplots_adjust(hspace=0.7)
draw()
pause(10)
