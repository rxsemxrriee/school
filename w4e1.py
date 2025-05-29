import matplotlib.pyplot as plt
import matplotlib as mlp
import numpy as np

x = np.arange(2000,2021)
y = np.random.randint(0,100,len(x))

print(x,y)
yaxis = plt.ylim(0,100)
plt.title("Generated profit for each year.")
plt.plot(x,y, color = 'g', marker=".")
plt.show()
