class MyException(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def example_exception():
    try:
        a = 1
        b = 0
        if b == 0:
            raise MyException("除数不能为0")
        res = a / b
        return res
    except MyException as e:
        print(e)


example_exception()
