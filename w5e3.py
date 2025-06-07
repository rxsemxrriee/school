import matplotlib.pyplot as plt

day = []
for i in range(1,6):
    day.append(f'Day {i}')
temp = [25,23,22,26,24]
plt.bar(day,temp,color="yellow")
for i,v in enumerate(temp):
    print(i,v)
    plt.text(i,v,str(v))
plt.title("Daily temperature")
plt.xlabel('Temperature in degree celcius')
plt.ylabel('Day')
plt.show()