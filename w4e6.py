import matplotlib.pyplot as plt
import numpy as np

a = np.arange(-10,11)
x = np.tan(a)
y = a**2 - 6 * a
z = 3 * a**2
w = a**2 - 3 * a + 7
plt.grid( )
plt.plot(a,x,linestyle='none',marker='.')
plt.show()

plt.grid( )
plt.plot(a,y,linestyle='none',marker='.')
plt.show()

plt.grid( )
plt.plot(a,z,linestyle='none',marker='.')
plt.show()

plt.grid( )
plt.plot(a,w,linestyle='none',marker='.')
plt.show()