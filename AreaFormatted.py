from numpy import *
from sys import version

if int(version[0])>2:
    raw_input = input
name = raw_input('Key in your name:')
print("Hi ",name)
radius = eval(raw_input('Enter a radius:'))
area = 2 * pi * radius ** 2
print('your radius is = %8.5f'%radius,' and area is = %f'%area)
outfile = open('A.dat','w')
outfile.write('r = %13.5f\n'%(radius))
outfile.write('A = %13.5f\n'%(area))
outfile.close()