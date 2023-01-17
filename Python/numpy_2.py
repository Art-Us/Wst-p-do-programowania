import numpy as np

liczby = np.random.randint(0, 51, (5, 5))
print(liczby)

print(f'max: {liczby.max()}')
print(f'max: {liczby.min()}')

print(f'max collumns: {liczby.max(axis = 1)}')
print(f'max rows: {liczby.max(axis = 0)}')

print(f'min collumns: {liczby.min(axis = 1)}')
print(f'min rows: {liczby.min(axis = 0)}')

