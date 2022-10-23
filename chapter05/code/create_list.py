# 方式一
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
list3 = [1, 2, "a"]
list4 = [1, 2, ["a", "b"]]

print(list1, type(list1))
print(list2)
print(list3)
print(list4)

# 方式二 传入序列即可
list5 = list("abc")
list6 = list([1,2,3])
print(list5)
print(list6)
