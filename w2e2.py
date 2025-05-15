import numpy as np

a = np.array([[1,1,1],[1,1,1]])
b = np.array([[2,2,2],[2,2,2]])
c = np.array([[2,2,2],[2,2,2],[2,2,2]])
print(np.hstack([a,b]))
print(np.vstack([a,b]))
print(np.concatenate([a,b]))
print(np.concatenate([b,c]))
print(np.hstack([a,c]))
print(np.hstack([b,c]))
print(np.vstack([a,c]))
print(np.vstack([b,c]))
