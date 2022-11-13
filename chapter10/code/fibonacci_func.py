l1 = [0, 1]


def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

res = fibonacci(5)
print(res)
# for i in range(1000):
#     l1.append(l1[len(l1)-1] + l1[len(l1)-2])
#
# print(l1)

# 非递归
def fibonacci(n):
    for i in range(n - len(l1)):  # n = 3 (0,1,2)
        l1.append(l1[len(l1) - 1] + l1[len(l1) - 2])


fibonacci(5)
print(l1[-1])
