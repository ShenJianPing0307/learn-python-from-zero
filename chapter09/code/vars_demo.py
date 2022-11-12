class A:
    pass


a = A()
a.name = 'zs'
print(a.__dict__)
print(vars(a))  # 返回对象object的属性和属性值的字典对象

print(str.__dict__)