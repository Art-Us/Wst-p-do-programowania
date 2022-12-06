x = list(range(1, 11))
print(x)
print(x[-3:])
x[:0] = x[-3:]
x[-3:] = []
print(x)
y = []
y = x[:]
print(y)
y[1] = 100
print(y)