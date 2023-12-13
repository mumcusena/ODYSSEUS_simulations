import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load your data
data = pd.read_csv('all_basic_features.csv')
data = data[data['energy_ratio'] != 1]

# Separate features and target variable
X = data.drop('energy_ratio', axis=1)
y = data['energy_ratio']

# Split the data into training, validation, and test sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)

# Build and train the Random Forest Regressor model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)  # You can adjust n_estimators and other parameters
rf_model.fit(X_train_scaled, y_train)

# Evaluate the model on the test set
mse = mean_squared_error(y_test, rf_model.predict(X_test_scaled))
print(f'Mean Squared Error on Test Set: {mse}')

baseline_mse = np.mean((y - np.mean(y))**2)
print(f'Baseline Mean Squared Error: {baseline_mse}')

# Make predictions
predictions = rf_model.predict(X_test_scaled)

# Calculate the errors (residuals)
errors = y_test - rf_model.predict(X_test_scaled)

# Plot box plots for errors
plt.boxplot(errors)
plt.title('Box Plot of Errors on Test Set')
plt.ylabel('Errors')
plt.show()
