import flask


class A:

    def __call__(self, *args, **kwargs):
        """调用对象时执行"""
        print("__call__")
        self.get_age()

    def __new__(cls, *args, **kwargs):
        """生成对象self，先于init执行"""
        __instance = None
        if not __instance:
            __instance = super().__new__(cls)
        return __instance
    def __init__(self):
        """对象初始化,对象已经生成了"""
        self.age = 10
        print("init")
    def get_age(self):
        print(self.age)

class B:

    def __init__(self, app):
        self.app = app
    def get_age(self):
        self.app()

a1 = A()
b = B(a1)
b.get_age()


# print(id(a1))
# print(id(a2))

# class Log:
#     def __new__(cls, *args, **kwargs):
#         """生成对象self，先于init执行"""
#         # __instance = None
#         # if not __instance:
#         #     __instance = super().__new__(cls)
#         # return __instance
#         if not hasattr(cls,"instance"):
#             cls.instance = super(Log, cls).__new__(cls, *args, **kwargs)
#         return cls.instance
#
#     def print(self):
#         print("log")
#
#
# log1 = Log()
# log2 = Log()
#
# print(id(log1))
# print(id(log2))
