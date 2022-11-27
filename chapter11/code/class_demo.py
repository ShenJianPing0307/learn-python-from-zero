class Car:
    weight = 1.4

    def run(self):
        print(self)
        print("run...")
        pass


c1 = Car()
c2 = Car()

print(Car.weight)
print(c1.weight)
print(c2.weight)

Car.run(Car())
c1.run()
c2.run()
