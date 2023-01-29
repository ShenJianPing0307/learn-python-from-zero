data = [
    {"日期": "2022-01-12", "最高气温": 15, "最低气温": 8, "天气": "晴", "风向": "东北风"},
    {"日期": "2022-02-12", "最高气温": 12, "最低气温": 7, "天气": "晴", "风向": "东北风"},
    {"日期": "2022-02-15", "最高气温": 11, "最低气温": None, "天气": "多云", "风向": "西南风"},
    {"日期": "2022-03-09", "最高气温": None, "最低气温": 13, "天气": "晴", "风向": "西北风"},
    {"日期": "2022-03-13", "最高气温": 19, "最低气温": 15, "天气": "小雨", "风向": "北风"},
    {"日期": "2022-06-18", "最高气温": 28, "最低气温": 22, "天气": "小雨", "风向": "西南风"},
]
import pandas as pd

df = pd.DataFrame(data)

print(df)

# 查看是否存在缺失值
res = df.isna() # DataFrame.isnull is an alias for DataFrame.isna.
print(res)

# 填充缺失值
df1 = df.fillna(0)
df2 = df.fillna(df["最高气温"].mean())
df3 = df.fillna(method="pad")
print(df1)
print(df2)
print(df3)

# 删除行
df4 = df.dropna(axis=0)
print(df4)

# 删除列
df5 = df.dropna(axis=1)
print(df5)