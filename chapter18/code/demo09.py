data = [
    {"name": "apple", "price": 6, "quantity": 100},
    {"name": "pear", "price": 8.5, "quantity": 230},
    {"name": "banana", "price": 6, "quantity": 150},
]

import pandas as pd

df = pd.DataFrame(data)
print(df)


def add_price(row):
    """接收的就是df每一行数据"""
    if row["name"] == "pear":
        row["price"] = row["price"] + 1
    return row


df1 = df.apply(add_price, axis=1)
print(df1)

"""
for item in data:
    add_price(item)
"""
