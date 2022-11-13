
# 列表解析式
l1 = [i for i in range(10)]
print(l1)

# 列表生成式
l2 = (i for i in range(10, 20))
print(l2.__next__())
print(list(l2))

for i in l2:
    print(i)
