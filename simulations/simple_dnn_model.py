import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from keras import layers
import matplotlib.pyplot as plt


# Load your data
data = pd.read_csv('all_basic_features.csv')
# Assuming 'data' is your DataFrame
data = data[data['energy_ratio'] != 1]
# Now 'data' will contain only rows where 'energy_ratio' is not equal to 1
# Separate features and target variable
X = data.drop('energy_ratio', axis=1)
y = data['energy_ratio']

print(X)
print(y)
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build the model
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dense(32, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(16, activation='relu'),
    layers.Dense(16, activation='relu'),
    layers.Dense(16, activation='relu'),
    layers.Dense(1)  # Output layer with 1 neuron for regression
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
history = model.fit(X_train_scaled, y_train, epochs=50, batch_size=32, validation_data=(X_test_scaled, y_test))

# Evaluate the model on the test set
loss = model.evaluate(X_test_scaled, y_test)
print(f'Mean Squared Error on Test Set: {loss}')
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()
plt.show()
# Make predictions
predictions = model.predict(X_test_scaled)
