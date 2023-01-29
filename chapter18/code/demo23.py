data = {
    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie2', 'Indomie3'],
    'style': ['cup', 'cup1', 'cup2', 'pack', 'pack'],
    'rating': [4, 4, 3.5, 15, 15]
}

import pandas as pd

df = pd.DataFrame(data)
print(df)

# 判断是否存在重复行
res = df.duplicated(keep='last', subset=['brand'])
print(res)

# 删除重复行
df1 = df.drop_duplicates(keep='last', subset=['brand'])
print(df1)
