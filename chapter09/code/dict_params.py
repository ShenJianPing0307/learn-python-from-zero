# 关键字传参，字典接收
def bar(a, **kwargs):
    print(a)
    print(kwargs)


bar(1, b=2, c=3)


# 传递字典
def ha(a, **kwargs):
    print(a)
    print(kwargs)


ha(1, **{"b": 2, "c": 3})  # 两个 ** 解析字典
