# def dynamic(*args):
#     print(args)  # ('hello', 1, ['a', 'b', 'c'])


# dynamic("hello", 1, ['a', 'b', 'c'])




# def a(a, *args):
#     print(a)
#     print(args)
#     if args:  # ('abc',)
#         return "{}-{}".format(a, args[0])
#     return a
#
#
# res = a(1, "abc")
# print(res)

def a(*args, a):
    print(a)
    print(args)
    if args:  # ('abc',)
        return "{}-{}".format(a, args[0])
    return a

res = a(1, "abc", a=2)
print(res)