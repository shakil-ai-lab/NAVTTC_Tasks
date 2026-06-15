import numpy as np
import pandas as pd

try:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import accuracy_score, classification_report
except ImportError as e:
    raise ImportError(
        "Required packages not installed. Install tensorflow and scikit-learn: pip install tensorflow scikit-learn"
    ) from e

# MLP exercise using a synthetic classification dataset
X, y = make_classification(
    n_samples=220,
    n_features=8,
    n_informative=6,
    n_redundant=2,
    n_classes=2,
    random_state=42,
)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build MLP model
model = Sequential([
    Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid'),
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=30, batch_size=16, verbose=1)

# Evaluate and print results
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"MLP test accuracy: {accuracy:.4f}")

predictions = (model.predict(X_test) > 0.5).astype(int).squeeze()
print("Classification report:")
print(classification_report(y_test, predictions))
