import matplotlib.pyplot as plt

day = []
for i in range(1,11):
    day.append(f"Day {i}")
daytemp = [25,23,22,26,24,27,29,27,27,26]
nighttemp = [18,17,16,19,18,20,21,18,17,20]

plt.barh(day, nighttemp, color='blue')
plt.barh(day,daytemp,left=nighttemp,color='black')
plt.title("10 days temperature during the day and night")
plt.xlabel('Temperature (in Celcius)')
plt.ylabel('Days')
plt.legend(['Night','Day'])
plt.show()