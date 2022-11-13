l1 = [1, 2, 3]
l2 = [2, 3, 4]


# 单个可迭代对象
def f1(item):
    return item + 1


res = map(f1, l1)
print(list(res))
for i in res:
    print(i)


# 多个可迭代对象
def f2(item1, item2):
    return item1 * item2


res = map(f2, l1, l2)

print(list(res))

# lambda简易写法
res = map(lambda x, y: x * y, l1, l2)
print(list(res))
