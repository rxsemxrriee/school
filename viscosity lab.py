from mlxtend.regressor import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Data
dball = np.array([0.00318, 0.00398, 0.00477, 0.006, 0.00701])
dballsq = dball ** 2
terminalv = np.array([0.002, 0.0032, 0.0046, 0.0069, 0.0087])

# Reshape X to 2D for mlxtend
X = dballsq.reshape(-1, 1)
y = terminalv

# Fit model
lr = LinearRegression()
lr.fit(X, y)

# Predict for plotting
y_pred = lr.predict(X)

# Plot
plt.scatter(dballsq, terminalv, label='Data', marker='o')
plt.plot(dballsq, y_pred, color='red', label='Regression Line')
plt.xlabel("Diameter of the metal ball squared (m²)")
plt.ylabel("Terminal Velocity (Vt)")
plt.title("Terminal Velocity vs. Diameter Squared")
plt.legend()
plt.show()

# Print regression details
print(f"Slope: {lr.weights_[1]}")
print(f"Intercept: {lr.weights_[0]}")
