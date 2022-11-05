# 方式一

# d = {}
# print(type(d))  # <class 'dict'>
# d = {"name": "zhangsan"}
# print(d)

# 方式二
# d1 = dict()
# print(type(d1))  # <class 'dict'>
"""
        dict(iterable) -> new dictionary initialized as if via:
            d = {}
            for k, v in iterable:
                d[k] = v
"""

# d2 = dict([["k1", "v1"], ["k2", "v2"]])
# print(d2)  # {'k1': 'v1', 'k2': 'v2'}

# 字典的key是唯一的, 不会抛出异常，但是相同的键会被覆盖
d3 = {"name": "zhangsan", "name": "lisi"}
print(d3["name"]) # lisi