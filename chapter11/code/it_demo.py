l2 = [1, 2, 3]

# iter(l2)
# l2 = l2.__iter__()
# print(l2)
# l2.__next__()
# print(l2.__next__())
# print(l2.__next__())
# print(l2.__next__())

while True:
    try:
        l2 = l2.__iter__() # 转成迭代器
        print(l2.__next__())
    except StopIteration as e:
        break

