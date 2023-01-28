import pandas as pd

data = {"letter1": ['a', 'b'], "number": [1, 2]}
df = pd.DataFrame(data)
print(df)

data1 = {"letter2": ['c', 'd'], "number": [2, 4]}
df1 = pd.DataFrame(data1)
print(df1)

# on
df2 = pd.merge(df, df1) # 显式通过on
df3 = pd.merge(df, df1, on="number")
print(df2)

# left_on, right_on
data = {"letter1": ['a', 'b'], "number1": [1, 2]}
df = pd.DataFrame(data)
df["number1"] = [1, 2]
print(df)

data1 = {"letter2": ['c', 'd'], "number2": [2, 4]}
df1 = pd.DataFrame(data1)
df1["number2"] = [1, 2]
print(df1)

df4 = pd.merge(df, df1, left_on="number1", right_on="number2")
print("df4")
print(df4)