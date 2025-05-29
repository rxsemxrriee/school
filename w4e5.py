import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,1000000)
y = np.sin(x)
z = np.cos(x)
""" plt.grid()
plt.plot(x,y,color='b',label="y=sin(x)")
plt.plot(x,z,color='orange',label='z=cos(x)')
plt.legend()
plt.show() """

""" plt.grid(axis='x')
plt.plot(x,y,color='b',label="y=sin(x)")
plt.plot(x,z,color='orange',label='z=cos(x)')
plt.legend()
plt.show() """

plt.grid(axis='y')
plt.plot(x,y,color='b',label="y=sin(x)")
plt.plot(x,z,color='orange',label='z=cos(x)')
plt.legend()
plt.show()