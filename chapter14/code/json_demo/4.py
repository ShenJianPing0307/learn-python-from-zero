import json
user_info = {"name": "zhansan", "age": 20}
# 写入对象到文件
with open("4.txt", "w") as f:
    json.dump(user_info, f)

# 将文件中的对象读出
with open("4.txt") as f:
    res = json.load(f)
    print(res, type(res))
