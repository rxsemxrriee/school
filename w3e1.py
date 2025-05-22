import numpy as np

array1 = np.random.randint(1,1000,(10,10))
array2 = np.multiply(array1,3)
print(array1, '\n', array2)
print(np.amax(array2),np.amin(array2))
print(np.median(array2),np.mean(array2),np.average(array2))
for i in range(0,len(array2)):
    print(f"Max of row array2({i}): {np.amax(array2[i,:])}")
    print(f"Max of row array2({i}): {np.amax(array2[i,:])}")
    print(f"Max of column array2({i}): {np.amax(array2[:, i])}")
    print(f"Max of column array2({i}): {np.amax(array2[:, i])}")
