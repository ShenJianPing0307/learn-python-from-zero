# https://leetcode.cn/problems/palindrome-number/
num = 121321


def method(num):
    result = True
    s = str(num)
    if "-" in s:
        return False
    for i in range(len(s)):
        if str(num)[i] != str(num)[len(s) - 1 - i]:
            result = False
    return result


def method1(num):
    s = str(num)
    if "-" in s:
        return False
    l, r = 0, len(s) - 1
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


print(method1(num))
