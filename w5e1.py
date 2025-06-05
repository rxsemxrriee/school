import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(0, 100, (10, 10))
y = np.random.randint(0, 100, (10, 10))

clname = input('Enter a color name: ')
eclname = input('Enter an edge color name: ')
markerstyle = input('Enter a marker style: ')
markersize = int(input('Enter a marker size: '))  

plt.scatter(x, y, color=clname, marker=markerstyle, s=markersize, edgecolor=eclname)
plt.show()
