data = [["a", 12, 12],
        ["e", 12.3, 33],
        ["b", 12.3, 36],
        ["a", 1, 1]]

import pandas as pd

df = pd.DataFrame(data, columns=["d", "b", "c"])
print(df)

# df = df.groupby(by='d').sum()
# print(df)
"""
a  12.0  12
a   1.0   1

b  12.3  36

e  12.3  33
"""


def f1(df):
    print("df")
    print(df)

from pandas.core.groupby.generic import DataFrameGroupBy

df1 = df.groupby(by='d')
df1.apply(f1)
# print(df1)
