import pickle

user_info = {"name": "zhansan", "age": 20}
# 写入文件
f = open("1.txt", "wb")
pickle.dump(user_info, f)
f.close()

# 读出对象
f = open("1.txt", "rb")
res = pickle.load(f)
print(res)
f.close()