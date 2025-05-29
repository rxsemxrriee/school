import numpy as np

array1 = np.random.randint(10,size=(2,3))
array2 = np.random.randint(10,size=(2,3))



#print('Result of dot product:',np.dot(array1,array2))
print('Result of dot product:',np.inner(array1,array2))