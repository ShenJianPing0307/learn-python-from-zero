str1="this is mY PEN"
print(str1.title())

list1=str1.split()
str2="".join(list1)
print(str2)
set1=set(str2)
print(set1,len(set1))

"""
t:1
i:2
...
{"t":1, "i":2,...}
{"i":2, "t":1,...}
"""
# 第一步完成字典的数据结构 字母:数量
str1 = "this is mY PEN"
str2 = str1.replace(" ", "")
print(str2)
d1 = {}
# for i in str2:
#     d1[i] = d1.get(i, 0) + 1
# print(d1.items())

# for i in str2:
#     d1.setdefault(i, 0) # {"i":0} 第二次 i {"i": 1}
#     d1[i] += 1 # 0 + 1 = 1 {"i": 1}

for i in str2:
    if d1.get(i) is None: # None
        d1[i] = 0 # {"i":0}
    d1[i] += 1 # {"i":1}

def sort_value(x):
    return x[1]


order_d1 = sorted(d1.items(), key=sort_value, reverse=True)
print(order_d1[0:2])
