data = [
    {"name": "apple", "price": 6, "quantity": 100},
    {"name": "pear", "price": 8.5, "quantity": 230},
    {"name": "banana", "price": 6, "quantity": 150},
]
import pandas as pd


df = pd.DataFrame(data)


print(df)


df1 = df[0:1][["name", "price"]]
df2 = df[1:][["name", "price"]]
# df11 = df.loc[0:1, ["name", "price"]]  print(df11)
print(df1)
print(df2)

