list1 = [1, 2, 3]

# append
# list1.append(5)
# print(list1)


# clear
# list1.clear()
# print(list1)

# copy
# list2 = list1.copy()
# print(list2)
# print(id(list1))
# print(id(list2))

# count
# num = list1.count(2)
# print(num)

# extend
# list3 = ['a', 'b']
# list1.extend(list3)
# print(list1)
# 通过切片、列表连接 l1 + l3 也可以实现extend效果

# index
# print(list1.index(1))
# print(list1.index(5))

# insert 分片也可
# list1.insert(1, 10)
# print(list1)

# pop有返回值，返回值就是被弹出的元素，默认移除最后一个元素，也可以通过索引移除指定的元素，知道元素位置有这个
# list1.pop()
# print(list1)
# res = list1.pop(1)
# print(list1)
# print(res)

# remove 移除指定的元素，知道元素值用这个
# res = list1.remove(1)
# print(res) # None 无返回值
# print(list1)
# print(list1.remove(5)) # ValueError: list.remove(x): x not in list

# reverse
# list1.reverse() # [::-1]
# print(list1)

# sort
# list1.sort(reverse=False)
# print(list1)
#
# def compare(item):
#
#     return item["age"]

#
# list5 = [{"username": "zhangsan", "age": 15},
#          {"username": "lisi", "age": 13},
#          {"username": "wuwang", "age": 27}]
# # print("list5", list5)
# list5.sort(key=compare) # [15,13,27]
# print(list5)

# sorted
print(sorted(list1))
print(sorted(list1, reverse=True))


