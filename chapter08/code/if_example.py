print("输入两个数字做运算")
a = int(input())
b = int(input())


def rechener(a, b):
    print("输入需要的运算法则（+,-,*,/）")
    x = input()

    if "+" == x:
        res = a + b
        return res
    elif "-" == x:
        res = a - b
        return res
    elif "*" == x:
        res = a * b
        return res
    else:
        res = a / b
        return res


res = rechener(a, b)
print(res)
