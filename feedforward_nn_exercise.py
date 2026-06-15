import numpy as np
import pandas as pd

try:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import mean_squared_error
except ImportError as e:
    raise ImportError(
        "Required packages not installed. Install tensorflow and scikit-learn: pip install tensorflow scikit-learn"
    ) from e

# Feedforward neural network exercise on synthetic regression data
np.random.seed(42)
X = np.random.rand(300, 3) * 10
weights = np.array([1.5, -2.0, 3.0])
y = X.dot(weights) + 4.5 + np.random.randn(300) * 2.5

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = Sequential([
    Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(16, activation='relu'),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')

model.fit(X_train, y_train, epochs=40, batch_size=16, verbose=1)

predictions = model.predict(X_test).squeeze()
mse = mean_squared_error(y_test, predictions)
print(f"Feedforward NN regression MSE: {mse:.4f}")
print(pd.DataFrame({'Actual': y_test[:10], 'Predicted': predictions[:10]}))
