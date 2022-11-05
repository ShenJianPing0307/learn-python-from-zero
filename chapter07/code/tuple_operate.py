t1 = (1, 2, 3, 4, 5)

# 索引、切片取值
print(t1[0])  # 1
print(t1[1:3])  # 2, 3
# 元组相加
t2 = ("hello",)
print(t1 + t2)  # (1, 2, 3, 4, 5, 'hello')

# 元组相乘
print(t1 * 2)  # (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# in 运算
print(1 in t1)

# 内建函数
print(len(t1))
print(max(t1))
print(min(t1))

