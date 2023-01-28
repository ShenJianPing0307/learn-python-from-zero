import pandas as pd

data = {"letter": ['a', 'b'], "number": [1, 2]}
df = pd.DataFrame(data)
print(df)

data1 = {"letter": ['c', 'd'], "number": [3, 4]}
df1 = pd.DataFrame(data1)
print(df1)

# 行合并
print(pd.concat([df, df1], ignore_index=True))

# 列合并
df1.rename(columns={"letter": "letter1", "number": "number1"}, inplace=True)
print(pd.concat([df, df1], axis=1))
# df2 = pd.concat([df, df1], axis=1)
# df3 = df2.sort_values(by=["letter"])
# print(df3)
# print(df2["letter"], type(df2["letter"]))
# print(df2.loc[:, [0]])
