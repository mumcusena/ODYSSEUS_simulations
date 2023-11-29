import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from keras import layers
from keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt

# Load your data
data = pd.read_csv('all_basic_features.csv')

# Drop rows where energy_ratio is 1
data = data[data['energy_ratio'] != 1]

# Separate features and target variable
X = data.drop('energy_ratio', axis=1)
y = data['energy_ratio']
print(np.var(y))

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Define the number of folds for cross-validation
n_splits = 10
kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)

# Initialize arrays to store training and validation loss for each fold
all_train_loss = []
all_val_loss = []
mse_scores = []


# Perform cross-validation
for train_index, test_index in kf.split(X_scaled):
    X_train, X_temp, y_train, y_temp = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

    # Build the model
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
        layers.Dense(32, activation='relu'),
        layers.Dense(32, activation='relu'),
        layers.Dropout(0.3),
        layers.Dense(16, activation='relu'),
        layers.Dense(16, activation='relu'),
    ])

    # Compile the model
    optimizer = keras.optimizers.legacy.Adam(learning_rate=0.001)
    model.compile(optimizer=optimizer, loss='mean_squared_error')
    early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

    # Train the model
    history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_val, y_val), verbose=0)
    mse = model.evaluate(X_test, y_test, verbose=0)
    mse_scores.append(mse)
    # Store training and validation loss for each fold
    all_train_loss.append(history.history['loss'])
    all_val_loss.append(history.history['val_loss'])
    

# Calculate the average MSE across all folds
average_mse = np.mean(mse_scores)
print(f'Average Mean Squared Error across {n_splits} folds: {average_mse}')

mse_std_dev = np.std(mse_scores)
print(f'Standard Deviation of Mean Squared Error: {mse_std_dev}')

baseline_mse = np.mean((y - np.mean(y))**2)
print(f'Baseline Mean Squared Error: {baseline_mse}')

# Plot average training and validation loss
avg_train_loss = np.mean(all_train_loss, axis=0)
avg_val_loss = np.mean(all_val_loss, axis=0)

plt.plot(avg_train_loss, label='Average Training Loss')
plt.plot(avg_val_loss, label='Average Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Mean Squared Error')
plt.legend()
plt.show()