import pandas as pd

data = {"letter1": ['a', 'b'], "number": [1, 2]}
df = pd.DataFrame(data)
print(df)

data1 = {"letter2": ['c', 'd'], "number": [2, 4]}
df1 = pd.DataFrame(data1)
print(df1)

df3 = pd.merge(df, df1, left_index=True, right_index=True)
print(df3)