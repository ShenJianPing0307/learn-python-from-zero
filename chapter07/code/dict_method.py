d1 = {"name": "harry", "age": 20, "hobby": ["books", "pingpong"]}

d2 = {"addr": "german"}

d5 = dict(d1, **d2)  # {'name': 'harry', 'age': 20, 'hobby': ['books', 'pingpong'], 'addr': 'german'}
print(d5)

d3 = {"name": "weiwei"}

# d1.update(d2)  # 类似与列表中的extend
# print(d1)  # {'name': 'harry', 'age': 20, 'hobby': ['books', 'pingpong'], 'addr': 'german'}
#
# d1.update(d3)
# print(d1)  # {'name': 'weiwei', 'age': 20, 'hobby': ['books', 'pingpong'], 'addr': 'german'}


# d3 = {}
# res2 = d3.setdefault("name", "weiwei")
# print(res2)
# print(d3)
"""
weiwei
{'name': 'weiwei'}
"""

# res = d3.setdefault("name", "huihui")
# print(res)
# print(d3)
"""
weiwei
{'name': 'weiwei'}
"""

# res = d1.pop("name")
# print(res) # harry
# print(d1) # {'age': 20, 'hobby': ['books', 'pingpong']}
#
# res1 = d1.popitem()
# print(res1) # ('hobby', ['books', 'pingpong'])
# print(d1) # {'name': 'harry', 'age': 20}

# keys / values / items
# print(d1.keys())
# print(d1.values())
# print(d1.items())
"""
dict_keys(['name', 'age', 'hobby'])
dict_values(['harry', 20, ['books', 'pingpong']])
dict_items([('name', 'harry'), ('age', 20), ('hobby', ['books', 'pingpong'])])
"""

# get 取值
# print(d1.get("name")) # d1["name"]
# print(d1.get("mm"))
# print(d1.get("mm", "harry")) # 如果key不存在可以指定默认值


# fromkeys
# d2 = {}
# d3 = d2.fromkeys(["name", "age", "hobby"])
# print(d3)# {'name': None, 'age': None, 'hobby': None} d3[""name]= "xx"
# d4 = d2.fromkeys(["name", "age", "hobby"], "xx")
# print(d4) # {'name': 'xx', 'age': 'xx', 'hobby': 'xx'}


# clear
# d1.clear()
# print(d1)

# copy 与 deepcopy
import copy

# d2 = d1.copy()
# d1["age"] = 21
# print("d1", d1)
# print("d2", d2)
"""
d1 {'name': 'harry', 'age': 21, 'hobby': ['books', 'pingpong']}
d2 {'name': 'harry', 'age': 20, 'hobby': ['books', 'pingpong']}
"""

# d1["hobby"][0] = "fish"
# print("d1", d1)
# print("d2", d2)
"""
d1 {'name': 'harry', 'age': 21, 'hobby': ['fish', 'pingpong']}
d2 {'name': 'harry', 'age': 20, 'hobby': ['fish', 'pingpong']}
"""
