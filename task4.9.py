import random

n = int(input('N = '))
length = n if n > 10 else 10
a = [random.randint(0, length) for i in range(length)]
filtered = []

for index, number in enumerate(a):
    if number <= index:
        filtered.append(index)

print('N (filtered) =', filtered, a)