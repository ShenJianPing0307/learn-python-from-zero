import numpy as np

x = np.array([2,3,4,5]) # 一维数组

li = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
y = np.array(li) # 多维数组

z = np.array([
    [1,2,3],
    ['a', 'b', 'c']
])


print(x, type(x), x.dtype)
print(y, type(y), y.dtype)
print(z, type(z), z.dtype)


