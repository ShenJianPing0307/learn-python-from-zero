from flask import Flask, render_template
import os
import pandas as pd
import numpy as np

app = Flask(__name__)


def handle_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    file_dir = os.path.join(BASE_DIR, 'files')

    df1 = pd.read_csv(f"{file_dir}/dieselPricesInRomania.csv")
    df2 = pd.read_csv(f"{file_dir}/gasolinePricesInRomania.csv")
    df3 = pd.merge(df1, df2, on="date")
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

    df5 = df4.groupby(by='date').agg([np.sum, np.mean, np.max, np.min])

    """
    [
    {gasoline price per liter in RON amin:4.428},
    {diesel price per liter in RON sum:2046.488},
    ]
    
    """
    data = df5.to_dict(orient='records')
    price_data_list = []
    for item in data:
        for k, v in item.items():
            d1 = {}
            k1 = f'{k[0]} {k[1]}'
            d1[k1] = v
            price_data_list.append(d1)
    return price_data_list


@app.route('/index')
def index():
    data = handle_data()
    return render_template("index.html", data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8001)
