s1 = {1, 2, 3}
s2 = {1, 2, 4}


s1 = {1, 2, 3}
s2 = {1, 2}
s1.update(s2)
print(s1)

# union将集合的并集作为新集合返回
s1 = {1, 2, 3}
s2 = {1, 2}
print(s1.union(s2))

# 对称差集，先求交集，再求并集
s1 = {1, 2, 3}
s2 = {1, 2}
print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print(s1) # {3, 4}

s1 = {1, 2, 3}
print(s1.remove(2)) # None
print(s1) # {1, 3}

s1 = {1, 2, 3}
print(s1.pop()) # 1
print(s1) # {2, 3}

s1 = {1, 2, 3}
s2 = {1, 2}
print(s1.issuperset(s2)) # True

s1 = {1, 2, 3}
s2 = {1, 2}
flag = s2.issubset(s1)
print(s2.issubset(s1)) # True

# isdisjoint
s1 = {1, 2, 3}
s2 = {1, 2}
flag = s1.isdisjoint(s2)
print(flag) # False

# intersection \ intersection_update
s1 = {1, 2, 3}
s2 = {1, 2}
s3 = s1.intersection(s2)
s1.intersection_update(s2)
print(s3)
print(s1)

# discard
s1 = {1, 2, 3}
s1.discard(1)
print(s1)

# 效果等同于s1-s2，但是是操作原集合，无返回值
s1 = {1, 2, 3}
s2 = {1, 2}
s1.difference_update(s2)
print(s1)

# difference 求差集 相当于 s1-s2
s1 = {1, 2, 3}
s2 = {1, 2}
s3 = s1.difference(s2)
print(s3)  # {3}

# add
s1.add(4)
print(s1) # {1, 2, 3, 4}

# clear
# s1.clear()
# print(s1) # set()

# copy
s1 = {1, 2, 3}
print(s1)
s2 = s1.copy()
print(s2)
#
# s1.add(6)
# print("s1", s1)
# print("s2",s2)
