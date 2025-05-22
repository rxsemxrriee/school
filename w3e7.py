import numpy as np

row = int(input("Input rows:"))
cl = int(input('Input columns:'))
arr = np.random.randint(0,100,(row,cl))
print(arr)
print(arr.T)
print(np.linalg.det(arr))
print(np.linalg.inv(arr))

