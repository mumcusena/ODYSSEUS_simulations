import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load your data
data = pd.read_csv('../../feature_files/all_basic_features_spc_dist.csv')
data = data[data['energy_ratio'] != 1]

# Separate features and target variable
X = data.drop('energy_ratio', axis=1)
y = data['energy_ratio']

# Split the data into training, validation, and test sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

columns_to_scale = ['mass_den', 'atom_per_mol_1', 'atom_per_mol_2', 'atom_per_mol_3', 'atom_per_mol_4', 'atom_per_mol_5', 'mean_excit']  # Replace with your column names

# Select columns to keep unchanged
columns_to_keep = [col for col in X.columns if col not in columns_to_scale]

# Separate features for scaling and those to keep as they are
X_train_to_scale = X_train[columns_to_scale]
X_val_to_scale = X_val[columns_to_scale]
X_test_to_scale = X_test[columns_to_scale]

X_train_remaining = X_train[columns_to_keep]
X_val_remaining = X_val[columns_to_keep]
X_test_remaining = X_test[columns_to_keep]

# Standardize the selected columns only
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_to_scale)
X_val_scaled = scaler.transform(X_val_to_scale)
X_test_scaled = scaler.transform(X_test_to_scale)

# Concatenate standardized and unchanged columns
X_train_final = np.hstack((X_train_scaled, X_train_remaining.values))
X_val_final = np.hstack((X_val_scaled, X_val_remaining.values))
X_test_final = np.hstack((X_test_scaled, X_test_remaining.values))

# Define the hyperparameters and their values for searching
param_grid = {
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.01, 0.1, 0.5],
    'max_depth': [3, 4, 5]
    # You can add more parameters and their values to test
}

# Initialize the Gradient Boosting Regressor
gbm = GradientBoostingRegressor(random_state=42)

# Initialize GridSearchCV with the necessary parameters
grid_search = GridSearchCV(estimator=gbm, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)

# Fit the GridSearchCV to the data (using only the training set and validation set)
grid_search.fit(np.vstack((X_train_final, X_val_final)), pd.concat([y_train, y_val]))

# Get the best parameters found by GridSearchCV
best_params = grid_search.best_params_
print("Best Hyperparameters:", best_params)

# Retrain the Gradient Boosting Regressor with the best parameters using the combined training and validation data
best_gbm_model = GradientBoostingRegressor(**best_params, random_state=42)
best_gbm_model.fit(np.vstack((X_train_final, X_val_final)), pd.concat([y_train, y_val]))

# Evaluate the model on the test set
mse = mean_squared_error(y_test, best_gbm_model.predict(X_test_final))
print(f'Mean Squared Error on Test Set after Hyperparameter Tuning: {mse}')

# Make predictions
predictions = best_gbm_model.predict(X_test_final)

# Calculate the errors (residuals)
errors = y_test - best_gbm_model.predict(X_test_final)

# Plot box plots for errors
plt.boxplot(errors)
plt.title('Box Plot of Errors on Test Set')
plt.ylabel('Errors')
plt.show()
