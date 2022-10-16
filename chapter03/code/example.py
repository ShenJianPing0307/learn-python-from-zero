# 方法一
print("请输入一个三位数字:")
nummer = int(input())
a = int(nummer / 100)
b = int((nummer - 100 * a) / 10)
c = int((nummer - 100 * a - 10 * b))
res = a ** 3 + b ** 3 + c ** 3
print(res)

# 方法二
x = int(input("请输入一个三位数字:"))
a = x // 100 # 1
b = (x - a * 100) // 10
c = x % 10
res = a ** 3 + b ** 3 + c ** 3
print(res)
