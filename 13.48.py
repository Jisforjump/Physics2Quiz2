import math

h = float(input('enter height: '))
p = (float(input('enter gauge pressure: ')) +1) * 101325

v2 = math.sqrt(2 * (p - 101325 + 1025 * 9.8 * h) / 1025)
print(v2)