import pandas as pd

df1 = pd.DataFrame({"one": [0, 4, 8], "two": [1, 5, 9]})

print(df1)

# 获取块
df2 = df1.loc[0:1, ["one"]]
print(df2)

# 获取单个值
val = df1.loc[0, ["two"]]
print(val.values[0], type(val))

# 修改单个值
df1.loc[0, ["two"]] = 10
print(df1)
