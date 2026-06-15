import numpy as np
import pandas as pd

try:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense
    from tensorflow.keras.utils import to_categorical
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import accuracy_score, classification_report
except ImportError as e:
    raise ImportError(
        "Required packages not installed. Install tensorflow and scikit-learn: pip install tensorflow scikit-learn"
    ) from e

# Neural network exercise using a small multiclass classification dataset
X, y = make_classification(
    n_samples=250,
    n_features=10,
    n_informative=8,
    n_redundant=2,
    n_classes=3,
    n_clusters_per_class=1,
    random_state=42,
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
y_train_categorical = to_categorical(y_train)
y_test_categorical = to_categorical(y_test)

model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(32, activation='relu'),
    Dense(3, activation='softmax'),
])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train_categorical, epochs=30, batch_size=16, verbose=1)

loss, accuracy = model.evaluate(X_test, y_test_categorical, verbose=0)
print(f"Neural network test accuracy: {accuracy:.4f}")

predictions = model.predict(X_test)
y_pred = np.argmax(predictions, axis=1)
print("Classification report:")
print(classification_report(y_test, y_pred))
