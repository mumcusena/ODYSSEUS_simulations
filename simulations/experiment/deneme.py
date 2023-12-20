import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the exponential function
def exponential_function(x, a, b):
    return a * np.exp(b * x)

# Golden truths data
golden_truths = np.array([(0.03, 0.7659409907568246),
                          (0.06, 0.48045968631528235),
                          (0.09, 0.3392603557798375),
                          (0.12, 0.2308036110512369)])

# Predictions data
predictions = np.array([(0.03, 0.57703894),
                        (0.04, 0.5414538),
                        (0.05, 0.50122625),
                        (0.06, 0.45031005),
                        (0.07, 0.3961556),
                        (0.08, 0.34251827),
                        (0.09, 0.2719523),
                        (0.1, 0.19960693),
                        (0.11, 0.13728496),
                        (0.12, 0.09537722)])

# Extract x and y values
x_golden_truths, y_golden_truths = zip(*golden_truths)
x_predictions, y_predictions = zip(*predictions)

# Convert x values to NumPy array
x_golden_truths = np.array(x_golden_truths)
x_predictions = np.array(x_predictions)

# Fit an exponential curve to the golden truths
params, covariance = curve_fit(exponential_function, x_golden_truths, y_golden_truths)

# Generate y values for the fitted curve
y_fit_curve = exponential_function(x_golden_truths, *params)

# Plot the golden truths, fitted curve, and predictions
plt.scatter(x_golden_truths, y_golden_truths, label='Golden Truths', color='blue')
plt.plot(x_golden_truths, y_fit_curve, label='Fitted Exponential Curve', color='green')
plt.scatter(x_predictions, y_predictions, label='Predictions', color='red')

# Calculate deviations
deviations = y_predictions - exponential_function(x_predictions, *params)
for i, deviation in enumerate(deviations):
    plt.annotate(f'{deviation:.4f}', (x_predictions[i], y_predictions[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Set plot labels and legend
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

# Show the plot
plt.show()
