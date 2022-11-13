from functools import reduce

l1 = [i for i in range(100)]

# 不带初始值
# res = sum(l1)
# print(res)

# res = reduce(lambda x, y: x + y, l1) # 累积 [0,1,2...]
# print(res)

# 初始值
# res = reduce(lambda x, y: x + y, l1, 1000) # 初始值 1000
# print(res)

# 初始值cde
a = "abc"
b = "cde"
res = reduce(lambda x, y: x + y, a, b)
print(res) # cdeabc
