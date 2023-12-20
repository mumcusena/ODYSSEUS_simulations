import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV

# Load your data
data = pd.read_csv('../../feature_files/all_basic_features.csv')
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

# Define the hyperparameters and their values for searching
param_grid = {
    'max_depth': [None, 5, 10, 15],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
    # You can add more parameters and their values to test
}

# Initialize the Decision Tree Regressor
tree = DecisionTreeRegressor(random_state=42)

# Initialize GridSearchCV with the necessary parameters
grid_search = GridSearchCV(estimator=tree, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)

# Fit the GridSearchCV to the data (using only the training set and validation set)
grid_search.fit(np.vstack((X_train_scaled, X_val_scaled)), pd.concat([y_train, y_val]))

# Get the best parameters found by GridSearchCV
best_params = grid_search.best_params_
print("Best Hyperparameters:", best_params)

# Retrain the Decision Tree Regressor with the best parameters using the combined training and validation data
best_tree_model = DecisionTreeRegressor(**best_params, random_state=42)
best_tree_model.fit(np.vstack((X_train_scaled, X_val_scaled)), pd.concat([y_train, y_val]))

# Evaluate the model on the test set
mse = mean_squared_error(y_test, best_tree_model.predict(X_test_scaled))
print(f'Mean Squared Error on Test Set after Hyperparameter Tuning: {mse}')

# Make predictions
predictions = best_tree_model.predict(X_test_scaled)

# Calculate the errors (residuals)
errors = y_test - best_tree_model.predict(X_test_scaled)

# Plot box plots for errors
plt.boxplot(errors)
plt.title('Box Plot of Errors on Test Set')
plt.ylabel('Errors')
plt.show()
