import math
rate = float(input('enter rate: '))
r1 = float(input('enter radius 1: '))
p1 = float(input('enter absolute pressure: '))
r2 = float(input('enter radius 2: '))

A1 = (math.pi * r1 **2)
A2 = (math.pi * r2 **2)
v1 = rate / A1 * 0.01
v2 = rate / A2 * 0.01

p2 = p1 - 0.5 * 1000 * (v2 **2 - v1 **2)
print(f'{p2} Pa')