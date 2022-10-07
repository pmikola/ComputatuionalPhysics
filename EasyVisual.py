from vpython import *
import numpy as np
tgraph =graph(title="My graph", xtitle="x",ytitle="y")
f1 = gcurve(color = color.black)
#label(text = "Wykres przy użyciu lib Vpython")

f1=gdots()

for x in np.arange(0,10,0.01):
    f1.plot(pos = (x,5*cos(5*x)*exp(-0.4)))



