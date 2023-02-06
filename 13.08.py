import math

l = float(input('enter length: '))
rOuter = float(input('enter outer diameter: ')) / 2 * 0.01
rInner = float(input('enter inner diameter: ')) / 2 * 0.01

w = math.pi * l * (rOuter **2 - rInner **2) * 8900 * 9.8
print(w)