# 数据
data = {
    "name": "zhansan",
    "age": 20,
    "gender": "male"
}

# 定义一个模板
str1 = "{name}-{age}-{gender}"

# 把数据渲染到模板上
print(str1.format_map(data))