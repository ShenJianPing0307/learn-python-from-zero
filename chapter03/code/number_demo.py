# a = 10  # 整型
# print(type(a))  # int
#
# b = 10.2  # 浮点型
# print(type(b))  # float
#
# c = True  # bool
# d = False  # bool
# print(type(c), type(d))
#
# e = 2 + 3j
# print(type(e))  # complex
#
# print(1 + 2)
# print(3.6 - 1)
# print(True + 1)  # True相当于数字1，False相当于数字0
# print(False + 1)
#
# print(True == 1)  # True
# print(False == 0) # True

# 从终端接收两个数，输出两个数的乘积
# 1 * 1 = 1
# 1 * 2 = 2

print("请输入两个数字:")
a = input("a=")
b = input("b=")
print(type(a), type(b))
print(a,"*", b, "=" , int(a)*int(b))
