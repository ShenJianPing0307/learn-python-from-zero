user_info = {"name": "zs", "age": 20, "addr": "german"}

print(user_info.items())  # dict_items([('name', 'zs'), ('age', 20), ('addr', 'german')])

res = zip(user_info.keys(), user_info.values())
print(list(res))  # [('name', 'zs'), ('age', 20), ('addr', 'german')]
