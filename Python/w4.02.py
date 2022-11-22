import random

x = int(input('Podaj długośćlisty: '))
x2 = int(input('Podaj długośćlisty 2: '))
list1 = []
list2 = []
for i in range(x):
    list1.append(random.randint(1, 10))
print(list1)

for i in range(x2):
    list2.append(random.randint(5, 15))
print(list2)
sz = int(input("Co szukamy? "))

if sz in list1 and sz in list2:
    print('Liczba z zestawu 1 i 2')
elif not sz in list1 and sz in list2:
    print('Liczba z zestawu 2')
elif sz in list1 and not sz in list2:
    print('Liczba z zestawu 1')
else:
    print('Nie ma takiej liczby w obu zestawach')

zestaw1_2 = list1 + list2
print(zestaw1_2)
zestaw1_2.sort()
print(zestaw1_2)

