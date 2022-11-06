# s1 = {1,2,3}
#
# print(s1[0]) # 无法索引和切片

list1 = [i for i in range(10)]
print(list1)

list1.extend([j for j in range(5)])

print(list1)

print(set(list1), len(set(list1)))

# n = 0 # {0:2, 1:2, 5:1}
# for m in list1:
#     num = list1.count(m)
#     if num <= 1:
#         n += 1
