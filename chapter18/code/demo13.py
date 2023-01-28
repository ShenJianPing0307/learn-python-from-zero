import pandas as pd

s1 = pd.Series(['a', 'b'])
s2 = pd.Series(['c', 'd'])

s3 = pd.concat([s1, s2], ignore_index=True)

print(s3)
