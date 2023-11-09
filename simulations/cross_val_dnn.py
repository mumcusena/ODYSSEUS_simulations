import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from keras import layers

# Load your data
data = pd.read_csv('all_basic_features.csv')

# Drop rows where energy_ratio is 1
data = data[data['energy_ratio'] != 1]

# Separate features and target variable
X = data.drop('energy_ratio', axis=1)
y = data['energy_ratio']

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Define the number of folds for cross-validation
n_splits = 5
kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)

# Initialize an array to store cross-validation results
mse_scores = []

# Perform cross-validation
for train_index, test_index in kf.split(X_scaled):
    X_train, X_test = X_scaled[train_index], X_scaled[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    # Build the model
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
        layers.Dense(32, activation='relu'),
        layers.Dense(1)
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the model
    history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test), verbose=0)

    # Evaluate the model on the test set
    mse = model.evaluate(X_test, y_test, verbose=0)
    mse_scores.append(mse)
    

# Calculate the average MSE across all folds
average_mse = np.mean(mse_scores)
print(f'Average Mean Squared Error across {n_splits} folds: {average_mse}')
