import numpy as np

A = np.array([[1,1],
            [0,1]] )
B = np.array([[2,0],
            [3,4]] )

print(A * B)
                    # elementwise product
# array([[2, 0],
#        [0, 4]])
# >>> A @ B                       # matrix product
# array([[5, 4],
#        [3, 4]])
# >>> A.dot(B)                    # another matrix product
# array([[5, 4],
#        [3, 4]])