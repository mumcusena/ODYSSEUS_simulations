import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.multioutput import MultiOutputRegressor


# Load your data
data = pd.read_csv('all_basic_features_spc_dist_var.csv')
data = data[data['energy_ratio'] != 1]

# Separate features and target variable
X_train = data.drop(['energy_ratio', 'sigma'], axis=1)
y_train = data[['energy_ratio', 'sigma']] 


columns_to_scale = ['mass_den', 'atom_per_mol_1', 'atom_per_mol_2', 'atom_per_mol_3', 'atom_per_mol_4', 'atom_per_mol_5', 'mean_excit']  # Replace with your column names

# Select columns to keep unchanged
columns_to_keep = [col for col in X_train.columns if col not in columns_to_scale]

# Separate features for scaling and those to keep as they are
X_train_to_scale = X_train[columns_to_scale]

X_train_remaining = X_train[columns_to_keep]

# Standardize the selected columns only
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_to_scale)

# Concatenate standardized and unchanged columns
X_train_final = np.hstack((X_train_scaled, X_train_remaining.values))
# Define the hyperparameters and their values for searching
"""param_grid = {
    'C': [0.1, 1, 10],  
    'gamma': [0.1, 1, 10],
    'epsilon': [0.1, 0.2, 0.5]
    # Add more parameters to tune as needed
}

# Initialize the SVR model
svm = SVR(kernel='rbf')

# Initialize GridSearchCV with the necessary parameters
grid_search = GridSearchCV(estimator=svm, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)

# Fit the GridSearchCV to the data (using only the training set and validation set)
grid_search.fit(np.vstack((X_train_final, X_val_final)), pd.concat([y_train, y_val]))
"""
# Get the best parameters found by GridSearchCV
best_params = {'C': 10, 'gamma': 0.1, 'epsilon': 0.1}
print("Best Hyperparameters:", best_params)

# Retrain the SVR model with the best parameters using the combined training and validation data
best_svm_model = MultiOutputRegressor(SVR(**best_params, kernel='rbf'))
best_svm_model.fit(X_train_final, y_train)

# Evaluate the model on the test set

data2 = pd.read_csv('test_data_spc_dist.csv')

# Separate features and target variable
X_test = data2

predictions = best_svm_model.predict(X_test)

print(predictions)
