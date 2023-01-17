import numpy as np

liczby = np.zeros((3, 3))
liczby[1:, :2] = 1
print(liczby)
print("")

liczby = np.zeros((3, 3))
liczby[:, 2] = 1
print(liczby)
print("")

liczby = np.zeros((3, 3))
liczby[:2, :] = 1
print(liczby)
print("")

liczby = np.zeros((3, 3))
liczby[:2, 0] = 1
print(liczby)
print("")

liczby = np.zeros((3, 3))
liczby[:2,[0,2]] = 1
print(liczby)
print("")
