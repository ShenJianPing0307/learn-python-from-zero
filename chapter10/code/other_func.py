a = 10

# 一般方式
if a > 10:
    print("a大于10")
else:
    print("a小于等于10")

# 三元表达式
print("a大于10") if a > 10 else print("a小于等于10")


# 函数中使用三元表达式
def f1():
    a = 10
    return "a大于10" if a > 10 else "a小于等于10"
