class A:
    flag = "A"

    def func(self):
        print("a_func")


class B:
    flag = "B"

    def func(self):
        print("b_func")


class C:
    flag = "C"

    def func(self):
        print("c_func")


class D(A, B, C):
    flag = "D"


d = D()

print(d.flag)
d.func()
