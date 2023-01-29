import os
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file_dir = os.path.join(BASE_DIR, 'files')

df1 = pd.read_csv(f"{file_dir}/dieselPricesInRomania.csv")
df2 = pd.read_csv(f"{file_dir}/gasolinePricesInRomania.csv")

print(df1.head(5))
print(df2.head(5))

df3 = pd.merge(df1, df2, on="date")
print(df3)
# print(df3["date"].unique())
# 统计每一年的用油的总和

# df3["diesel price per liter in RON"].sum()
d1 = {}  # {"2020":4.333, "2021":200,}


def handle_row(row):
    year = row['date'].rsplit(maxsplit=1, sep='-')[-1]
    d1[year] = d1.get(year, 0) + row['diesel price per liter in RON']
    return row


def handle_row_1(row):
    row['date'] = row['date'].rsplit(maxsplit=1, sep='-')[-1]
    return row


# df3.apply(handle_row, axis=1)
df4 = df3.apply(handle_row_1, axis=1)
print(df4)

df5 = df4.groupby(by='date').agg([np.sum, np.mean, np.max, np.min])

print(df5)

df5.to_excel(f"{file_dir}/PricesOutput.xlsx")

