p = float(input('enter pressure: ')) * 100000

h = p / (13600 * 9.8) * 100
print(f'{h} cm')