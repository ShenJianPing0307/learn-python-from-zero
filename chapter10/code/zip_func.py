# res = zip('abcdefg', range(3))
#
# print(list(res)) # [('a', 0), ('b', 1), ('c', 2)]

"""
输入：
flower flow flew
求取 多个单词 的公共前缀
"""

first = "flower"
second = "flow"
third = "flew"

prefix = ""
res = zip(first, second, third)
print(res)

for i in res:
    print(i)
    if len(set(i)) == 1:
        prefix += i[0]
    else:
        break
print(prefix)


# res = ""
# for i in first:
#     for x in second:
#         for y in third:
#             if i==x==y:
#                 res += i
#             else:
#                 break
#
# print(res)


