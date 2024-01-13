import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
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

best_params = {'n_estimators': 300, 'learning_rate': 0.1, 'max_depth': 5}  # You can use your best parameters here
best_gbm_model = MultiOutputRegressor(GradientBoostingRegressor(**best_params, random_state=42))
best_gbm_model.fit(X_train_final, y_train)


data2 = pd.read_csv('test_data_spc_dist.csv')

# Separate features and target variable
X_test = data2


# Evaluate the model on the test set

# Make predictions
predictions = best_gbm_model.predict(X_test)

print(predictions)