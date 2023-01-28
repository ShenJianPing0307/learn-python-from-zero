import pandas as pd
import numpy as np

# 1、ndarray构建DataFrame
df = pd.DataFrame(np.arange(12).reshape(3, 4))
# print(df)
# print(type(df))
"""
   0  1   2   3  # 列标签（列索引）
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
行索引
"""

# 2、字典（dict）
df1 = pd.DataFrame({"one": [0, 4, 8], "two": [1, 5, 9]})
# print(df1)
df2 = pd.DataFrame({"one": [0, 4, 8], "two": [1, 5, 9]}, index=["a", "b", "c"])
# print(df2)
# print(type(df2["one"]))


# 3、Series构建DataFrame
data = {"one": pd.Series([0, 4, 8], index=["a", "b", "c"]), "two": pd.Series([1, 5, 9], index=["a", "b", "c"])}
df3 = pd.DataFrame(data)
print(df3)
