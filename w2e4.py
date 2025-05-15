import numpy as np

array1 = np.array([[1,2,3,3,2],
                   [4,5,6,7,8],
                   [7,8,9,7,3],
                   [10,11,12,1,2],
                   [13,14,15,5,6],
                   [16,17,28,3,4]], dtype=int)

print(np.array_split(array1, 2, axis=1))
print(np.hsplit(array1, [3]))