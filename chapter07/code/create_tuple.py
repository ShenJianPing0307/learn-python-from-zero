# 第一种创建方式
t1 = (1, 2, 3, 4, 5)
print(type(t1)) # <class 'tuple'>

# 第二种创建方式
t2 = tuple([1,2,3])
print(t2)

# 注意
t3 = (5)
print(type(t3)) # <class 'int'>
t4 = (5,)
print(type(t4)) # <class 'tuple'>