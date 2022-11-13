l1 = [i for i in range(1000)]

res = filter(lambda x: x % 2 == 0, l1)
print(list(res))
