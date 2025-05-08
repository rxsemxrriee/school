import numpy as np

arr = np.array([[(19,20,21),(22,23,24),(25,26,27)],
               [(10,11,12),(13,14,15),(16,17,18)],
                [(1,2,3),(4,5,6),(7,8,9)]], dtype=int)
print(arr[0,1,1:3])
print(arr[1,1:3,0:2])
print(arr[2,0:3,0])
print(arr[0,2,0:3])