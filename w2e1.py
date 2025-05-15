import numpy as np
array1 = np.arange(2,101,2)
array2 = np.reshape(array1, (10,5))
array3 = np.reshape(array1, (5,2,5))
array4 = np.reshape(array1, (25,2))
print(array1)
print(array2)
print(array3)
print(array4)
