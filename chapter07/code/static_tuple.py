import timeit

print(timeit.timeit("list1 = [1,2,3]")) # 0.049630199995590374
print(timeit.timeit("t1 = (1,2,3)")) # 0.012114499986637384
