w = float(input('enter weight: '))
T = float(input('enter tension: '))
Fb = w - T

V = Fb / (9.8 * 1000)
print(V)

rho = w / (V * 9.8)
print(rho)