import pandas as pd

data = [
    {"name": "apple", "price": 6, "quantity": 100},
    {"name": "pear", "price": 8.5, "quantity": 230},
    {"name": "banana", "price": 6, "quantity": 150},
]

df = pd.DataFrame(data)
print(df)
print(type(df))
df["price"] = df["price"]+1
avr = df["price"].mean()
print(df)
print(avr)
