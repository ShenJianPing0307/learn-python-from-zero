list1 = ["abc", 6, [1, 2, 3]]


class A:
    pass


class B(A):
    pass


b = B()

print(isinstance(b, A))
# "print('abc')"

# 判断一个列表是否有int类型
# for i in list1:
#     if isinstance(i, int):
#         print("包含整型", i)
#     elif isinstance(i, str):
#         print("包含字符串", i)
