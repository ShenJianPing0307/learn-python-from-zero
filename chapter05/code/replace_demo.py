# s = "hello world"

# s = s.replace("world", "xiaoliu")
# s1 = s.replace("zhangsan", "lisi")
# print(s1)

# s = "hello world hello world"
#
# s1 = s.replace("world", "xiaoliu") # 默认替换全部
# s2 = s.replace("world", "xiaoliu", 1)
# print(s2)

# 脱敏 *
password = "123456789"
text = "打架、斗殴、你好"

password = password.replace(password, "*********")
text = text.replace("打架、斗殴", "*****")
print(password)
print(text)