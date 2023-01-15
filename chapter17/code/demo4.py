import numpy as np

arr = np.array([i for i in range(1, 10)]).reshape(3, 3)


arr1 = arr + 1
print(arr1)
print(arr1[0][0], type(arr1[0][0]))
