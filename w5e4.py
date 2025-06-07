import matplotlib.pyplot as plt

day = []
for i in range(1,6):
    day.append(f'Day {i}')
temp = [25,23,22,26,24]
for i,v in enumerate(temp):
    print(i,v)
    plt.text(v+0.3,i,str(v))
plt.barh(day,temp,color='red')
plt.show()