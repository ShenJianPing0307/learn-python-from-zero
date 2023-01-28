data = [
    {"name": "apple", "price": 6, "quantity": 100},
    {"name": "pear", "price": 8.5, "quantity": 230},
    {"name": "banana", "price": 6, "quantity": 150},
]

import pandas as pd

df = pd.DataFrame(data)
print(df)


def handle_cell(ele):
    if isinstance(ele, str):
        ele = ele + "_fruit"
    return ele


df1 = df.applymap(handle_cell)

print(df1)
