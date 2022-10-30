nums = [2, 7, 11, 15]
target = 9


def twoSum(nums, target):
    hashmap = {}  # 字典
    for index, num in enumerate(nums):  # [(0,2),(1,7),(2,11),(3,15)]
        hashmap[num] = index  # hashmap = {2:0, 7:1, 11:2, 15:3}
    for i, num in enumerate(nums):  # [(0,2),(1,7),(2,11),(3,15)]
        j = hashmap.get(target - num)  # hashmap = {2:0, 7:1, 11:2, 15:3}
        if j is not None and i != j:  # i=0 j=1
            return [i, j]


res = twoSum(nums, target)
print(res)
