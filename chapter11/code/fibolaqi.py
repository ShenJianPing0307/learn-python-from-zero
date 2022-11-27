class Fib:

    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        """iter(self)"""
        return self

    def __next__(self):
        """
        0 1 = 1 1
        1 3
        :return:
        """
        res = self.a
        self.a, self.b = self.b, self.a + self.b
        return res


f = Fib()

for i in f:
    print(i)
    if i > 10:
        break
