import math

m1 = float(input('enter the mass of car: '))
m2 = float(input('enter the mass of platform: '))
F1 = float(input('enter force the worker exerts: '))
d1 = float(input('enter diameter 1: '))

m = m1 + m2
F2 = m * 9.8
A1 = math.pi * (d1/2)**2
A2 = F2/F1 * A1
d2 = math.sqrt(A2 / math.pi) * 2
print(d2 * 0.01)

h1 = float(input('enter how much the worker pushes down: '))
h2 = A1/A2 * h1
print(h2 * 10)