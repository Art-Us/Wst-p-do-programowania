#1. Konwersja 8-bitowej liczby binarnej na liczbę dziesiętną.
#• Utwórz 8-elementową listę składaną o wartościach będących kolejnymi potęgami dwójki - [128 64 32
#16 8 4 2 1]
import numpy as np

a = int(input())
lista = [2**i for i in range(a-1, -1, -1)]
print(lista)

wagi = np.array(lista)
print(wagi)


licba_bin = np.random.randint(0, 2, a)
print(licba_bin)

wynik = licba_bin*wagi
print(wynik)
print(sum(wynik))