import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.arange(-10,11)
y1 = np.multiply(x,1)
y2 = np.multiply(x,2)
y3 = np.multiply(x,3)
y4 = np.multiply(x,4)
yaxis = plt.ylim(-40,40)
plt.plot(x,y1,marker='o',color='b')
plt.plot(x,y2,marker='o', ms=5,linestyle='-',color='y')
plt.plot(x,y3,marker='*', linestyle='-.',color='b')
plt.plot(x,y4,linestyle=':',color='r')
plt.show()