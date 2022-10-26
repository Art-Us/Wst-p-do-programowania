co_robimy = input('''Jaką operację chcesz wykonać?
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie
Wpisz numer operacji: ''')
ar1 = int(input('Podaj argument 1 '))
ar2 = int(input('Podaj argument 2 '))
if co_robimy == "1":
    res=ar1+ar2
elif co_robimy == "2":
    res=ar1-ar2
elif co_robimy == "3":
    res=ar1*ar2
elif co_robimy == "4":
    if ar2==0:
        res = "błąd, nie możemy dzielić na zero"
    else:
        res = ar1 / ar2
elif co_robimy == "5":
    res=ar1**ar2
else:
    res="błąd"
print(f'Wynik: {res}')
