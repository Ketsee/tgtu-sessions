from math import *

m = 2
t = 1.2
c = -1
b = 0.7

f = (m * tan(t) + abs(c * sin(t))) ** (1/3)
z = m * cos(b * t * sin(t)) + c

print('f =', f)
print('z =', z)
