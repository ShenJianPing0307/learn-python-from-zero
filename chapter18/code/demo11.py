data = [
    {"name": "apple", "price": 6, "quantity": 150},
    {"name": "pear", "price": 8.5, "quantity": 30},
    {"quantity": 100},
]

import pandas as pd

df = pd.DataFrame(data)
print(df)
print(df.columns)
print(df.loc[:, ["name", "quantity"]])
print(df.loc[:, ::2])
print(df[["name", "quantity"]])

# df.sort_index(ascending=False, inplace=True)
# print(df)

df.sort_values(by=["price"], inplace=True)
print(df)
print(df.index)  # [2, 0 ,1] [0, 1, 2] {2:0, 0:1, 1:2}

print(df[0:1])
