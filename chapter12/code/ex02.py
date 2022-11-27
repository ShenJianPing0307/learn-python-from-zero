def example_exception():
    try:
        a = 1
        b = 0
        res = a / b
        return res
    except ZeroDivisionError as e:
        print(e)
        print("除数不能为0")
    finally:
        print("程序执行完毕!")


res = example_exception()
print(res)
