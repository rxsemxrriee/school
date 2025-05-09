import numpy as np

array = np.array([(1,2,3,3,2),
                  (4,5,6,7,8),
                  (7,8,9,7,3),
                  (10,11,12,1,2),
                  (13,14,15,5,6),
                  (16,17,28,5,4)], dtype=int)

print(array)
print(array[0:3,0])
print(array[0:3,2])
print(array[0:3,4])
print(array[0:6,1])
print(array[0:6,4])
