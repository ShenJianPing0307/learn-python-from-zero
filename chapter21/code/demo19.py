# https://leetcode.cn/problems/roman-to-integer/
def romanToInt(s):
    roma = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
    total = 0
    for i, v in enumerate(s):
        cur = roma[s[i]]
        try:
            next = roma[s[i + 1]]
            if cur >= next:
                total += cur
            else:
                total -= cur
        except IndexError:
            total += cur

    return total


if __name__ == '__main__':
    s = "LVIII"
    print(romanToInt(s))
