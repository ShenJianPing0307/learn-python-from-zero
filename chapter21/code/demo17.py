# https://leetcode.cn/problems/two-sum/
nums = [11, 2, 17, 7]
target = 9


def twoSum(nums, target):
    for i, v1 in enumerate(nums):

        for j, v2 in enumerate(nums[i + 1:]):

            if v1 + v2 == target:
                return [i, i + j + 1]
    return []



def twoSum1(nums, target):
    for i, v1 in enumerate(nums):
        v2 = target - v1
        for j, v3 in enumerate(nums[i + 1:]):
            if v2 == target:
                return [i, i + j + 1]
    return []


if __name__ == '__main__':
    res = twoSum(nums, target)
    print(res)
