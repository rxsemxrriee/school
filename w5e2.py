import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([45, 78, 82, 23, 56, 29, 75, 96, 1, 29, 33])
y1 = np.array([90, 92, 64, 12, 52, 45, 35, 82, 57, 38, 74])
colors1 = np.linspace(0, 100, len(x1))  

x2 = np.array([45, 96, 1, 29, 45, 71, 66, 34, 82, 52, 33])
y2 = np.array([90, 82, 57, 38, 23, 19, 66, 56, 45, 25, 74])
colors2 = np.linspace(0, 100, len(x2))

fig, axs = plt.subplots(1, 2, figsize=(12, 6))
fig.suptitle("Scatter plot with different datasets")

scatter1 = axs[0].scatter(x1, y1, c=colors1, cmap='Accent', marker='o')
axs[0].set_title("Subplot 1")

scatter2 = axs[1].scatter(x2, y2, c=colors2, cmap='Accent', marker='s')
axs[1].set_title("Subplot 2")
cbar = plt.colorbar(scatter2, ax=axs[1])  

plt.tight_layout()
plt.show()
