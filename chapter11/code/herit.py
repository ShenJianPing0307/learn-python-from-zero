class Animal:

    def __init__(self, age):
        self.age = age

    def eat(self):
        print("eat")


class Dog(Animal):

    def __init__(self, age, name):
        super(Dog, self).__init__(age) # 初始化父类的实例变量
        self.name = name

    def noise(self):
        print("noise")


dog = Dog(age=10, name="xiaohuang")
print(dog.age)
