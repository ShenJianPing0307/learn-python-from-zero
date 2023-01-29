import os

data = [
    {"日期": "2022-01-12", "最高气温": 15, "最低气温": 8, "天气": "晴", "风向": "东北风"},
    {"日期": "2022-02-12", "最高气温": 12, "最低气温": 7, "天气": "晴", "风向": "东北风"},
    {"日期": "2022-02-15", "最高气温": 11, "最低气温": 9, "天气": "多云", "风向": "西南风"},
    {"日期": "2022-03-09", "最高气温": None, "最低气温": 13, "天气": "晴", "风向": "西北风"},
    {"日期": "2022-03-13", "最高气温": 19, "最低气温": None, "天气": "小雨", "风向": "北风"},
    {"日期": "2022-06-18", "最高气温": 28, "最低气温": 22, "天气": "小雨", "风向": "西南风"},
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file_path = os.path.join(BASE_DIR, 'files', 'output.xlsx')

import pandas as pd

df = pd.DataFrame(data)

df.fillna(0, inplace=True)

df.to_excel(file_path)
