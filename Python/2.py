x = int(input("x= "))
y = int(input("y= "))
z = int(input("z= "))

if (x > y) and (x > z):
    if y > z:
        print(z, y, x)
    else:
        print(y, z, x)
elif (y > x) and (y > z):
    if x > z:
        print(z, x, y)
    else:
        print(x, z, y)
else:
    if x > y:
        print(y, x, z)
    else:
        print(x, y, z)
