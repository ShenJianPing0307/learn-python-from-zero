d1 = {"name": "harry", "age": 20, "hobby": ["books", "pingpong"]}
# d2 = {}


# 增加键值对
# d1["addr"] = "German"
# print(d1)

# 修改值，键是必须存在的，假如不存在相当于增加键值对
# d1["age"] = 22
# print(d1)
# d1["xx"] = "xx"
# print(d1)

# 查询，这种通过dict[key]查询的话，如果key不存在就会报 KeyError 错误
# print(d1["age"])  # 22
# print(d1["mm"]) # KeyError: 'mm'

# 删除键值对 del dict[key]
# print(d1)
# del d1["name"]
# print(d1)

# key in dict
"""
if condition:
    pass
elif condition:
    pass
else:
    pass
"""
# if "mm" in d1:
#     del d1["mm"]
# else:
#     print("key不存在")
# print(d1)

# len(dict)
print(len(d1))