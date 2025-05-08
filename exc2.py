import numpy as np

arr3d = np.array([
                    [(1,2,3),(4,5,6),(9,6,5)],
                    [(7,8,9),(0,1,2),(5,7,0)],
                    [(6,3,2),(8,3,6),(3,7,1)]
                    ], dtype=float)
print(arr3d, "\n")
print(f'size: {arr3d.size}')
print(f'len: {len(arr3d)}')
print(f"shape: {np.shape(arr3d)}\n")
print(arr3d.astype(int))