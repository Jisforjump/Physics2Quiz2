import math
d = float(input('enter depth: '))

p = 1030 * 9.8 * d
print(p)

r = float(input('enter diameter: ')) / 2 * 0.01
A = math.pi * r **2
F = p * A
print(F)

F2 = 101325 * A
print(F2)