import matplotlib.pyplot as plt
import numpy as np

day = []
for i in range(1,11):
    day.append(f"Day {i}")
daytemp = [25,23,22,26,24,27,29,27,27,26]
nighttemp = [18,17,16,19,18,20,21,18,17,20]

height = 0.25

bar1 = np.arange(len(daytemp))
bar2 = bar1 + height

plt.barh(bar1,daytemp,height=height)
plt.barh(bar2,nighttemp,height=height)
plt.title("10 days temperature during the day and night")
plt.xlabel('Temperature (in Celcius)')
plt.ylabel('Days')
plt.yticks(bar1+0.15,day)
plt.legend(['Day Temperature','Night temperature'])
plt.show()