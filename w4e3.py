import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0,21,200000)
print(x)
a = np.sin(x)
b = np.cos(x)
c = np.tan(x)
plt.xlim(0,20)
plt.ylim(-5,5)
plt.plot(x,a,color='g')
plt.plot(x,b,color='b')
plt.plot(x,c,color='r')
plt.legend(loc='upper center')
plt.grid()
plt.show()

