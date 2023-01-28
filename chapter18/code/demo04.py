import pandas as pd

ser_obj1 = pd.Series([1, 2, 3], index=["a", "b", "c"])
ser_obj = pd.Series({"a": 1, "b": 2, "c": 3})

print(ser_obj1)
# 索引操作
# print(ser_obj.index)
# print(ser_obj.index[1])
# 值操作
# print(ser_obj.values)

# 预览数据
# print(ser_obj.head(2))
