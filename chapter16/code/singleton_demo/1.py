# # 单例模式
class A:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(A, cls).__new__(cls, *args, **kwargs)
        return cls._instance



a1 = A()
a2 = A()

print(id(a1))
print(id(a2))



