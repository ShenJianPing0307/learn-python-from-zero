class A:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "姓名：{}，年龄：{}".format(self.name, self.age)

a = A("zhangsan", 12)

print(a)
