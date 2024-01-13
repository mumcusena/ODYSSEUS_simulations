import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from keras import layers
import matplotlib.pyplot as plt

# Load your data
data = pd.read_csv('all_basic_features_spc_dist_var.csv')
data = data[data['energy_ratio'] != 1]

# Separate features and target variable
X = data.drop(['energy_ratio', 'sigma'], axis=1)  # Drop 'energy_ratio' and 'sigma' as input features
y = data[['energy_ratio', 'sigma']]  # Target columns - 'energy_ratio' and 'sigma'

print(np.var(y))
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

# Build the model
model = keras.Sequential([
    layers.Dense(133, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dense(133, activation='relu'),
    layers.Dropout(0.3),

    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),


    layers.Dense(32, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(16, activation='relu'),

    layers.Dense(8, activation='relu'),
    layers.Dense(8, activation='relu'),
    layers.Dense(8, activation='relu'),
    layers.Dense(8, activation='relu'),
    layers.Dense(8, activation='relu'),
    layers.Dense(8, activation='relu'),
    layers.Dense(8, activation='relu'),
    layers.Dense(8, activation='relu'),

    layers.Dense(4, activation='relu'),
    layers.Dense(4, activation='relu'),
    layers.Dense(4, activation='relu'),
    layers.Dense(4, activation='relu'),
    layers.Dense(4, activation='relu'),
    layers.Dense(4, activation='relu'),
    layers.Dense(4, activation='relu'),
    layers.Dense(4, activation='relu'),
    layers.Dense(4, activation='relu'),
    layers.Dense(4, activation='relu'),

    layers.Dense(2, activation='relu'),
    layers.Dense(2, activation='relu'),
    layers.Dense(2, activation='relu'),
    layers.Dense(2, activation='relu'),
    layers.Dense(2, activation='relu'),
    layers.Dense(2, activation='relu'),
    layers.Dense(2) # Output layer with 2 neuron for regression
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
history = model.fit(X_train_final, y_train, epochs=100, batch_size=32, validation_data=(X_val_final, y_val))

# Evaluate the model on the test set
loss = model.evaluate(X_test_final, y_test)
print(f'Mean Squared Error on Test Set: {loss}')

baseline_mse = np.mean((y - np.mean(y))**2)
print(f'Baseline Mean Squared Error: {baseline_mse}')

# Plot training and validation loss
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()
plt.show()


# Make predictions
predictions = model.predict(X_test_final)

errors_energy_ratio = y_test['energy_ratio'] - predictions[:, 0]
errors_sigma = y_test['sigma'] - predictions[:, 1]

# Plot box plots for errors
plt.boxplot([errors_energy_ratio, errors_sigma])
plt.title('Box Plot of Errors on Test Set')
plt.ylabel('Errors')
plt.xticks([1, 2], ['Energy Ratio', 'Sigma'])
plt.show()

errors_energy_ratio2 = (y_test['energy_ratio'] - predictions[:, 0]) / y_test['energy_ratio']
errors_sigma2 = y_test['sigma'] - predictions[:, 1] / y_test['sigma']

# Plot box plots for errors
plt.boxplot([errors_energy_ratio2, errors_sigma2])
plt.title('Box Plot of Errors on Test Set')
plt.ylabel('Errors')
plt.xticks([1, 2], ['Energy Ratio', 'Sigma'])
plt.show()