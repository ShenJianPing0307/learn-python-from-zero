import pandas as pd

# list创建
ser_obj = pd.Series([1, 2, 3, 4, 5])
print(ser_obj)
print(type(ser_obj))

# dict创建
ser_obj1 = pd.Series({"a": 1, "b": 2, "c": 3})
print(ser_obj1)
print(type(ser_obj1))
