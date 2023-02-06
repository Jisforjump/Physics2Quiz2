v1 = float(input('enter velocity 1: '))
p1 = float(input('enter pressure 1: '))
h = 0-float(input('enter height: '))

v2 = v1 / 4

p2 = p1 - 1000 * 9.8 * h - 0.5 * 1000 * (v2 **2 - v1 **2)
print(p2)