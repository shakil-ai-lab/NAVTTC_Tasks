import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Synthetic binary classification dataset
X, y = make_classification(
    n_samples=150,
    n_features=4,
    n_informative=3,
    n_redundant=0,
    n_clusters_per_class=1,
    flip_y=0.05,
    class_sep=1.2,
    random_state=42
)

# Convert to DataFrame
feature_names = [f'Feature_{i+1}' for i in range(X.shape[1])]
clf_df = pd.DataFrame(X, columns=feature_names)
clf_df['Target'] = y
print('Logistic Regression dataset sample:')
print(clf_df.head())
print()

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print('Accuracy:', accuracy_score(y_test, y_pred))
print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))
print('Classification Report:')
print(classification_report(y_test, y_pred))
