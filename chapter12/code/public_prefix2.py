strs = ["flower", "flow", "flight"]

"""
1、找出长度最小的字符串
   1.1 {3:"flow", }
   1.2 列表排序
2、
"""

res = sorted(strs, key=lambda item: len(item))
min_length = len(res)  # 每个字符串的最小长度

s = set()
res = ""
"""
1、取出每一个字符串
2、把每一个字符串的每个字母进行比较
"""
for i in range(min_length):
    for item in strs:
        s.add(item[i])  # "flower","flow","flight"
    if len(s) == 1:
        res += s.pop()
    else:
        break
    s.clear()

print(res)
