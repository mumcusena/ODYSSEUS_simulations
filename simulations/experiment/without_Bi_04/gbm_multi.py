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
X = data.drop(['energy_ratio', 'sigma'], axis=1)
y = data[['energy_ratio', 'sigma']] 

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

best_params = {'n_estimators': 300, 'learning_rate': 0.1, 'max_depth': 5}  # You can use your best parameters here
best_gbm_model = MultiOutputRegressor(GradientBoostingRegressor(**best_params, random_state=42))
best_gbm_model.fit(X_train_final, y_train)

# Evaluate the model on the test set
mse = mean_squared_error(y_test, best_gbm_model.predict(X_test_final))
print(f'Mean Squared Error on Test Set after Training: {mse}')

# Make predictions
predictions = best_gbm_model.predict(X_test_final)

# Calculate the errors (residuals) for each target variable
errors_energy_ratio = y_test['energy_ratio'] - predictions[:, 0]
errors_sigma = y_test['sigma'] - predictions[:, 1]

# Plot box plots for errors of each target variable
plt.boxplot([errors_energy_ratio, errors_sigma])
plt.title('Box Plot of Errors on Test Set for Energy Ratio and Sigma')
plt.ylabel('Errors')
plt.xticks([1, 2], ['Energy Ratio', 'Sigma'])
plt.show()