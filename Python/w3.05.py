ls = int(input("Ile mamy studentów: "))
a=0
i=1
b=0
while i<=ls:
    a=int(input("Liczba punktów: "))
    b=b+a
    i+=1
s=b/ls
print(f'Liczba punktów {b}, śriednia liczba punktów studenta {s}')