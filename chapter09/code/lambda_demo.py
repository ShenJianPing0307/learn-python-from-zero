import random

l1 = [i for i in range(1000)]
l2 = [j for j in range(1000)]

random.shuffle(l1)
random.shuffle(l2)

dict1 = {}
for i in range(1000):
    dict1[l1[i]] = l2[i]

print(dict1)
print(dict1.items())  # [(438, 497), (64, 228), (154, 368)...]

res = sorted(dict1.items(), key=lambda x: x[0])
print(res)

# def f1(item):
#     return item[0]
#
#
# res = sorted(dict1.items(), key=f1)
# print(res)
