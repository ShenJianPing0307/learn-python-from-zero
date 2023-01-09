import json

user_info = [{"name": "zhansan", "age": 20}, {"name": "lisi", "age": 21}]

res = str(user_info)

print(res, type(res))
print(json.dumps(user_info))



res1 = json.loads(res)
print(res1, type(res1))