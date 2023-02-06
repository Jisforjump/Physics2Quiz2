import math

r1 = float(input('enter radius: '))
rate = float(input('enter volume flow rate: '))
A1 = math.pi * r1 **2

v1 = rate / A1
print(v1)

v2 = float(input('enter water speed at second point: '))
A = rate / v2
r2 = math.sqrt(A / math.pi)
print(r2)