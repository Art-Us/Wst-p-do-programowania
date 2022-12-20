sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}
# print(sample_dict)
# for k in sample_dict:
#    print(k, sample_dict[k])


for k,v in sample_dict.items():
    print(f"{k:<10}: {v:>10}")

L = ['age', 'name', 'adb']
D = {}
# for k in L:
#  if k in sample_dict:
#   D[k] = sample_dict[k]
# print(D)

for k in L:
 if k in sample_dict:
  del sample_dict[k]         #print(sample_dict.pop(k.None))
print(sample_dict)

