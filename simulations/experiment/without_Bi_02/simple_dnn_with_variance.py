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
X_train = data.drop(['energy_ratio', 'sigma'], axis=1)  # Drop 'energy_ratio' and 'sigma' as input features
y_train = data[['energy_ratio', 'sigma']]  # Target columns - 'energy_ratio' and 'sigma'

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
history = model.fit(X_train_final, y_train, epochs=20, batch_size=32)

data2 = pd.read_csv('test_data_spc_dist.csv')

# Separate features and target variable
X_test = data2


# Evaluate the model on the test set

# Make predictions
predictions = model.predict(X_test)

print(predictions)
