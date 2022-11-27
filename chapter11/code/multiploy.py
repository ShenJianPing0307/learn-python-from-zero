import abc


class Animal(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def eat(self):
        pass

    @abc.abstractmethod
    def sleep(self):
        pass


class Dog(Animal):

    def eat(self): print("eat")

    def sleep(self):print("sleep")


d = Dog()
d.eat()
