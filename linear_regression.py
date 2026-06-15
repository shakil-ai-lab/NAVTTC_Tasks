import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Synthetic regression dataset
np.random.seed(42)
X = np.random.rand(100, 1) * 10
noise = np.random.randn(100, 1) * 3
y = 2.5 * X.squeeze() + 7 + noise.squeeze()

# Convert to DataFrame for readability
reg_df = pd.DataFrame({'Feature': X.squeeze(), 'Target': y})
print('Linear Regression dataset sample:')
print(reg_df.head())
print()

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print('Linear Regression results:')
print(f'Coefficient: {model.coef_[0]:.4f}')
print(f'Intercept: {model.intercept_:.4f}')
print(f'Mean Squared Error: {mse:.4f}')
print(f'R^2 Score: {r2:.4f}')
print()
print('Test values vs predictions:')
print(pd.DataFrame({'Actual': y_test, 'Predicted': predictions}).head())
