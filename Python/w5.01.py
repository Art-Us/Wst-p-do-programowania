values = [10, 20, 30]
keys = ["ten", "twenty", "thirty"]
# d = dict(zip(keys, values))
# print(list(zip(keys, values)))
# print(d)
#
# slownik ={}
# d = {}
# for i in range(0, len(keys)):
#     d[keys[i]] = values[i]
# print(d)
D = {keys[i]:values[i] for i in range(0, len(keys))}

print(D)


d2 = dict(thirty = 30, forty = 40, fifti = 50)
print(d2)
d3 = {}
d2.update(D)
print(d2)
