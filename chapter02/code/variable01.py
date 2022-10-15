# a = 10
# b = 10
# c = 10
#
# a = b = c = 10
# print(a,b,c)

# a = 10
# b = 20
# c = 30

# a, b, c = 10, 20, 30
# print(a, b, c)

# a , b = 10 , 20
# temp = a
# a = b
# b = temp
# print(a, b)

a , b = 10 , 20
a, b = b, a
print(a, b)
print(id(a), id(b))