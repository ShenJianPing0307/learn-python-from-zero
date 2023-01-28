import pandas as pd

df1 = pd.DataFrame({"one": [0, 4, 8], "two": [1, 5, 9]})

# 获取列
print(df1['one'])

# 添加列
df1["three"] = [7, 8, 9]
print(df1)

# 删除列
df1.drop(["three"], axis=1, inplace=True)
print(df1)
