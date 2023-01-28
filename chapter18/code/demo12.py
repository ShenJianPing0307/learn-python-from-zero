data = [
    {"name": "apple", "price": 6, "quantity": 150},
    {"name": "pear", "price": 8.5, "quantity": 30},
    {"quantity": 100},
]

import pandas as pd

df = pd.DataFrame(data)
print(df)

# print(df.count(axis=1))
# print(df.describe(include='all'))
print(df["price"].min())
print(df["price"].max())
print(df["price"].mean())
print(df["price"].sum())



