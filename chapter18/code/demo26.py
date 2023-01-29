import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file_path = os.path.join(BASE_DIR, 'files', 'output.xlsx')

df = pd.read_excel(file_path)

print(df)
