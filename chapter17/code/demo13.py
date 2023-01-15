import numpy as np


x = np.arange(12).reshape(3, 4)
# 数组级别循环
for row in x:
    print(row, type(row)) # 循环每一行
# 元素级别循环
for ele in x.flat:
    print(ele, type(ele))