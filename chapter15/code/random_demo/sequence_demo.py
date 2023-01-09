import random

# seq = [i for i in range(5)]
#
# print(random.choice(seq)) # 从序列中随机返回一个元素，如果是个空序列出现 IndexError错误

# population = [1, 2, 3, 4, 5, 6]
# print(random.sample(population, 2)) # 返回从集合或者列表中返回k个元素的列表，一般用于随机抽样

seq = [i for i in range(1000)]

print(seq)

random.shuffle(seq) # 打乱顺序

print(seq)