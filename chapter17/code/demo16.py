import numpy as np

arr = np.array([[1, 2], [2, 4]])

print(np.all(arr))
print(np.any(arr))
print(np.unique(arr))
arr1 = np.arange(10)
print(np.where(arr1 < 5, arr1, 10*arr1))

