import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

# Synthetic dataset for neural network demonstration
X, y = make_classification(
    n_samples=200,
    n_features=10,
    n_informative=8,
    n_redundant=2,
    n_clusters_per_class=2,
    random_state=42
)

feature_names = [f'Feature_{i+1}' for i in range(X.shape[1])]
nn_df = pd.DataFrame(X, columns=feature_names)
nn_df['Target'] = y
print('Neural Network dataset sample:')
print(nn_df.head())
print()

# Split and scale data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build simple dense neural network
model = Sequential([
    Dense(16, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train_scaled, y_train, epochs=25, batch_size=16, verbose=0)

# Evaluate
loss, accuracy = model.evaluate(X_test_scaled, y_test, verbose=0)
print(f'Neural network accuracy: {accuracy:.4f}')

# Predict and print classification report
y_pred = (model.predict(X_test_scaled) > 0.5).astype(int).squeeze()
print('Classification report:')
print(classification_report(y_test, y_pred))
