class Person:
    height = 170  # 类变量

    def __init__(self, name, age):
        "初始化对象，当对象创建好后，会执行这个方法"
        self.name = name  # 实例变量
        self.age = age  # 实例变量

    def run(self):
        print("实例方法--")

    @classmethod
    def eat(cls):
        print("类方法--")

    @staticmethod
    def study():
        print("静态方法--")


# # 类变量  类和实例都可以调用
p1 = Person('zs', 10)
print(Person.height)
print(p1.height)
#
# # 实例变量 类不可以调用, 实例可以
p2 = Person('zs', 10)
print(p2.name)
print(Person.name)  # AttributeError: type object 'Person' has no attribute 'name'

# 实例方法 类不可以调用, 实例可以
p3 = Person("wangwu", 20)
p3.run()
Person.run()  # TypeError: Person.run() missing 1 required positional argument: 'self'

# 类方法 类和实例都可以调用
p4 = Person("wangwu", 20)
p4.eat()
Person.eat()

# 静态方法 类和实例都可以调用
p5 = Person("wangwu", 20)
p5.study()
Person.study()
