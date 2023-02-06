import math

rhoair = 1.2
r = float(input('enter radius: ')) * 0.01
V = 4/3 * 3.14 * r** 3

Fb = rhoair * V * 9.8
print(Fb)

mBalloon = float(input('enter mass of balloon: ')) * 0.001
mTotal = V * 0.166 + mBalloon
Fg = mTotal * 9.8

Fnet = Fb - Fg
print(Fnet)