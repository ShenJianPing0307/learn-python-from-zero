import copy

list1 = ["abc", 6, [1, 2, 3]]
list2 = list1.copy()
list3 = copy.deepcopy(list1)
print(list2)
print(list3)
"""
['abc', 6, [1, 2, 3]]
['abc', 6, [1, 2, 3]]
"""
list2[2][0] = 11
print(list1)

# list1[0] = 9
# list1[2][0] = 10
# print()
# print(list2)
# print(list3)
"""
['abc', 6, [10, 2, 3]]
['abc', 6, [1, 2, 3]]
"""

