user_info = [{"name": "zhansan", "age": 20}, {"name": "lisi", "age": 21}]

import json

# 把一个对象转成字符串，这个过程被称为序列化
res = json.dumps(user_info)
print(type(res), res)

# 序列化后的字符串，可以存储
with open("2.txt", mode="w") as f:
    f.write(res)


# 读出序列化的结果
with open("2.txt") as f:
    res1 = f.read()

# 反序列化，从字符串转成对象
res2 = json.loads(res1)
print(res2, type(res2))