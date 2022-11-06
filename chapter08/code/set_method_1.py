# s1 = {1, 2, 3}
# s2 = {5, 6, 7}
#
# print(s1.union(s2))
# print(s1 | s2)

# s1 = {1, 2, 3}
# s2 = {2, 6, 7}
#
# print(s1.intersection(s2))
# print(s1 & s2)

# s1 = {1, 2, 3}
# s2 = {2, 6, 7}
#
# print(s1.difference(s2))
# print(s1 - s2)

# s1 = {1, 2, 3}
# s2 = {2, 6, 7}
#
# print(s1.symmetric_difference(s2))
# print(s1 ^ s2)

s1 = {1, 2, 3}
s2 = {2}

print(s2.issubset(s1))
print(s2 < s1)