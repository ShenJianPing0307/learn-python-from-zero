import os

print(os.name) # 可以用于开发或者生产的配置参数设置
print(os.environ) # 本地环境的配置参数
print(os.sep) # 路径分隔符, win "\" linux "/"
print(os.linesep)  # 行终止符 win "\r\n" linux "\n"
print(os.pathsep)  # 分隔文件路径的字符串 win ; linux :