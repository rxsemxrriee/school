import numpy as np

arr = np.array([4,1,2,1,6,7,7,2,8,9,0,5,2,3])
print(np.where(arr == 2))
# There is 1 array from the output
# There are 3 elements in the array
print(f"Minimum index is {np.amin(np.where(arr==2))}")

