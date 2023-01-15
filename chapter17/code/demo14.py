import numpy as np

arr = np.random.randn(2, 3)
arr1 = np.random.randn(2, 3)
print(arr)

print(np.ceil(arr)) # 向上取整
print(np.floor(arr)) # 向下取整
print(np.rint(arr)) # 四舍五入
print(np.isnan(arr)) # 判断是否为NaN

print(np.multiply(arr, arr1)) # 相乘
print(np.divide(arr, arr1)) # 相除