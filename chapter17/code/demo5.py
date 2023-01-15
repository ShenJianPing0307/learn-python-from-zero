import numpy as np

x = np.float32(1.0)


y = np.int_([1,2,3])


z = np.array([1,2,3], dtype=np.uint8)

z1 = z.astype(float)
print(z1, z1.dtype)
