import numpy as np

arrayrand = np.random.randint(0, 101, (5,5))
print(arrayrand, '\n')

arrayi = np.eye(5,5)
print(arrayi, '\n')

print(np.matmul(arrayrand, arrayi))