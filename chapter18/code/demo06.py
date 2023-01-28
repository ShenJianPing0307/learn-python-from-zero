import pandas as pd

df1 = pd.DataFrame({"one": [0, 4, 8], "two": [1, 5, 9]})
# df2 = pd.DataFrame({"one": [0, 4, 8], "two": [1, 5, 9]}, index=["a", "b", "c"])

# print(df2)

# 获取行
# print(df2.index)
# print(df2[0:1])
# print(df1[0:1])

# 添加行
df1 = df1.append({"one": 10, "three": 15}, ignore_index=True)
print(df1)

# 删除行
df2 = df1.drop([0], axis=0)
print(df2)

df1.drop([0], axis=0, inplace=True)
print(df1)
# 删除列
df3 = df1.drop(["one"], axis=1)

# df1 = []
#
# f1(deepcopy(df1))
# f2(deepcopy(df1))
