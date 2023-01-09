import pickle

user_info = {"name": "zhansan", "age": 20}

res = pickle.dumps(user_info)  # 序列化后是一串二进制
print(res)

print(pickle.loads(res))

