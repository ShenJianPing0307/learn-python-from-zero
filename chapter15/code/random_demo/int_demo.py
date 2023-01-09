import random

print(random.randrange(5))  # [0, 5)整数
print(random.randrange(4, 10))  # [4, 10) 整数
print(random.randrange(4, 10, 2)) # [4, 10] 偶数整数

print(random.randint(4, 10)) # [4, 10] 相当于 randrange(a, b+1) 对称分布

print(random.expovariate(0.3)) #指数分布

print(random.normalvariate(4, 0.5)) # 正态分布


