data = [
    {"日期": "2022-01-12", "最高气温": 15, "最低气温": 8, "天气": "晴", "风向": "东北风"},
    {"日期": "2022-02-12", "最高气温": 12, "最低气温": 7, "天气": "晴", "风向": "东北风"},
    {"日期": "2022-02-15", "最高气温": 11, "最低气温": 9, "天气": "多云", "风向": "西南风"},
    {"日期": "2022-03-09", "最高气温": 18, "最低气温": 13, "天气": "晴", "风向": "西北风"},
    {"日期": "2022-03-13", "最高气温": 19, "最低气温": 15, "天气": "小雨", "风向": "北风"},
    {"日期": "2022-06-18", "最高气温": 28, "最低气温": 22, "天气": "小雨", "风向": "西南风"},
]

import pandas as pd

df = pd.DataFrame(data)
print(df)

# 过滤出最高气温大于15的数据
# df1 = df[df["最高气温"] > 15]
# print(df1)

# 逻辑运算符过滤
df2 = df[(df["最高气温"] > 15) & (df["最低气温"] > 15)]
df3 = df[(df["最高气温"] > 15) | (df["最低气温"] > 15)]
df4 = df[df["最高气温"] != 15]
df5 = df[~(df["最高气温"] > 15)] # 取反

from pandas.core.strings.accessor import StringMethods

# 正则过滤
res = df[df["最高气温"].astype(str).str.contains('^2\d+', regex=True)]
print(res)

# 正则提取
df6 = df["日期"].str.extract(r'(\d+)')
print(df6)