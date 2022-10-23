# s1 = "abc"
# center
# print(s1.center(30, "*"))

# find

# s2 = "abcabc"
#
# print(s2.find("bc"))  # 1
# print(s2.find("bc", 2))  # 4
# print(s2.find("bc", 2, 6))  # 4
# print(s2.find("ac"))  # -1

# 字符串、列表，可迭代（可以循环）
# s1 = "abc"
# # for i in s1:
# #     print(i)
# # join 一般用于列表，把列表中的元素转成字符串
# list1 = ['a', 'b', 'c'] # s = "a-b-c"
# s = "-".join(list1)
# print(s)
# print(s1.join("def")) # 类似于拼接的效果s1.join(["d","e","f"])

s1 = "a-b-c"
print(s1.split())  # ['a-b-c']
print(s1.split("-"))  # ['a', 'b', 'c']
print(s1.split("-", 1))  # ['a', 'b-c']
