def example():
    yield 1 # return
    yield 2
    yield 3
e = example()
print(e.__next__())
print(e.__next__())
print(e.__next__())

from collections import Generator

print(isinstance(e, Generator))
