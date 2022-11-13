l1 = []

for i in range(1, 101):
    l1.append(i)
print(l1)

# 列表解析式
l2 = [i for i in range(1, 101)]
print(l2)

# 列表解析式加入条件判断
l3 = [i for i in range(1, 101) if i % 2 == 1]
print(l3)

# 列表解析式加入多重循环
l4 = [i + j for i in "ABC" for j in "XYZ"]  # ABC是外层循环
print(l4)
