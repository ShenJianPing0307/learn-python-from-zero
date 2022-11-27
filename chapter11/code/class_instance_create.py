class A:

    def __init__(self):
        """对对象进行初始化"""
        self.age = 10

    def __setattr__(self, key, value):
        """__dict__ = {"age":10}"""
        self.__dict__[key] = value

    def __getattr__(self, item):
        """如果属性不存在会被调用"""
        print("item",item)
        return self.__dict__.get(item)

    # def __getattribute__(self, item):
    #     print("__getattribute__", item)
    #     return self.__dict__.get(item)


a = A()

print(getattr(a, "age"))

