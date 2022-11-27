# 捕捉特定的异常
def example_exception():
    try:
        a = 1
        b = 0

        res = a / b
        return res
    except ZeroDivisionError as e:
        print(e)
        print("除数不能为0")


# 捕捉所有的异常
def example_exception1():
    try:
        a = 1
        b = 0

        res = a / b
        return res
    except:
        # print(e)
        print("出现异常")


# 捕捉所有的异常，得到详细信息
def example_exception2():
    try:
        a = 1
        b = 0

        res = a / b
        return res
    except Exception as e:
        print(e)


res = example_exception2()
print(res)
