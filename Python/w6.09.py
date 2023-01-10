import random
l1 = []
l2 = []
l3 = []
for i in range(10):
    l1.append(random.randint(0, 10))
    l2.append(random.randint(0, 10))
print(l1)
print(l2)

def intersection(l1, l2):
    for i in l1:
        if i in l2:
            l3.append(i)
    return l3
print(intersection(l1, l2))