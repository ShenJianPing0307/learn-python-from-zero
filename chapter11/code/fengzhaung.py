# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# p = Person("lily", 20)
# p.age = 30  # 可以修改变量值
# print(p.age)


class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


p = Person("lily", 20)
print(p.get_name())
