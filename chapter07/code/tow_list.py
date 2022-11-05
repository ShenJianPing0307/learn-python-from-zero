ll1 = [1, 2, 3, 4, 5]
ll2 = ["a", "b", "c", "d", "e"]

ll3 = []

for i in range(len(ll1)):
    ll3.append([ll1[i], ll2[i]])

print(ll3) # [[1, 'a'], [2, 'b'], [3, 'c'], [4, 'd'], [5, 'e']]
print(dict(ll3)) # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
# dict([[1,"a"],[]])

# res = zip(ll1, ll2)
# print(type(res))
# print(list(res))
# d = dict(list(res))
# print(d)
# print(type(list(res)), list(res))

# def a():
#     yield 1
#     yield 2
#
# a = a()
# print(type(a))
# print(next(a))
# print(next(a))
# print(next(a))
