import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

for row in arr:
    print(row)

for col in arr.T:
    print(col)