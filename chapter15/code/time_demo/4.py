import time

print(time.time())  # 时间戳

# 将当前时间戳转成结构化时间
print(time.localtime())  # 结构化时间
print(time.gmtime())  # 结构化时间

# 将结构时间转成时间戳
print(time.mktime(time.localtime()))

# 将结构化时间转成格式化时间
print(time.strftime("%Y-%m-%d"))  # 格式时间

# 将格式化时间转成结构化时间
print(time.strptime("2023-01-07 15:10", "%Y-%m-%d %H:%M"))  # 结构时间
