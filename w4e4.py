import matplotlib.pyplot as plt
import numpy as np

x = []
for i in range(1,11):
    x.append(f"Day {i}")

dtime = [25,23,22,26,24,27,29,27,27,26]
ntime = [18,17,16,19,18,20,21,18,17,20]

plt.title('10 Days Temperature', color="y")
plt.xlabel('Day',color='g')
plt.ylabel('Degree Celcius',color='g')
plt.plot(x,dtime,color='b',marker='.',ms=5)
plt.plot(x,ntime,color='black',linestyle=':',marker=".")
plt.show()