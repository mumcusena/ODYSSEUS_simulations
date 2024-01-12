import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Data points
x_values = np.array([0.3, 0.6, 0.9, 1.2, 1.3, 1.4, 1.5, 2.0])
y_values = np.array([0.7659, 0.480385, 0.339249, 0.2307941, 0.2161765, 0.195598, 0.180554146, 0.1103759])

# Labels for the data points
labels = ["0.3 mm", "0.6 mm", "0.9 mm", "1.2 mm", "1.3 mm", "1.4 mm", "1.5 mm", "2.0 mm"]

# Fit a curve to the data
def fit_function(x, a, b, c):
    return a * np.exp(-b * x) + c

params, _ = curve_fit(fit_function, x_values, y_values)

# Plotting
plt.figure(figsize=(10, 6))

# Plot each point individually with a different color and label
for i in range(len(x_values)):
    plt.scatter(x_values[i], y_values[i], label=f'{labels[i]}: ({x_values[i]}, {y_values[i]})')

# Plot the curve
x_fit = np.linspace(min(x_values), max(x_values), 100)
y_fit = fit_function(x_fit, *params)
plt.plot(x_fit, y_fit, label='Fitted Curve', color='black')

# Adding legend, title, and labels
plt.legend()
plt.title('Data Points and Fitted Curve')
plt.xlabel('X Values (mm)')
plt.ylabel('Y Values')
plt.grid(True)

# Show the plot
plt.show()