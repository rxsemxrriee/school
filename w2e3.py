import numpy as np

array1 = np.array([[1,2,3,3,2],
                   [4,5,6,7,8],
                   [7,8,9,7,3],
                   [10,11,12,1,2],
                   [13,14,15,5,6],
                   [16,17,28,3,4]], dtype=int)

print(f'array_split:{np.array_split(array1,3 )}')
print(f'vsplit:{np.vsplit(array1, 2)}')