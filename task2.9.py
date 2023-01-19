from math import *

a = 20.3
x = float(input('x = '))

if x > 1:
    f = log(x + 1)
else:
    f = sin(sqrt(abs(a * x))) ** 2

print('f =', f)