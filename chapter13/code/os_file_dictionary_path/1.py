import os

print(os.path.abspath("1.py")) # 返回绝对路径
print(os.path.split("test1/test2/1.txt")) # 将路径分隔，以元组的形式返回 ('test1/test2', '1.txt')
print(os.path.dirname("test1/test2/1.txt")) # 返回目录的路径
print(os.path.basename("test1/test2/1.txt")) # 返回路径最后的文件名
print(os.path.join("test1", "test2")) # 拼接路径
print(os.path.exists("test1/test2/3.txt")) # 判断文件是否存在
print(os.path.isdir("test1/test2/3.txt")) # 判断是否是目录
print(os.path.isfile("test1/test2/2.txt")) # 判断给定的路径是否是文件

print(os.path.getsize("test1/test2/2.txt")) # 获取给定目录或者文件的大小
print(os.path.getatime("test1/test2/2.txt")) # 最后文件访问时间
print(os.path.getmtime("test1/test2/2.txt")) # 最后文件修改时间
print(os.path.getctime("test1/test2/2.txt")) # 文件创建时间