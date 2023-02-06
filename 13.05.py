import math

price = float(input('how much million dollar of gold: ')) * 1000000

r = math.cbrt(price * 31.1035 / 1400 / 19.3 * 3 / (4 * math.pi))
print(r * 2)

price2 = 4/3 * math.pi * r ** 3 * 10.5 * 20 / 31.1035
print(price2)
