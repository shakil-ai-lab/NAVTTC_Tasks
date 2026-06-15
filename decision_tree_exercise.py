import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Synthetic dataset for decision tree exercise
X, y = make_classification(
    n_samples=160,
    n_features=5,
    n_informative=4,
    n_redundant=1,
    n_clusters_per_class=2,
    random_state=0
)

feature_names = [f'Feature_{i+1}' for i in range(X.shape[1])]

dt_df = pd.DataFrame(X, columns=feature_names)
dt_df['Target'] = y
print('Decision Tree dataset sample:')
print(dt_df.head())
print()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

model = DecisionTreeClassifier(max_depth=4, random_state=0)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('Decision Tree evaluation:')
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Classification Report:')
print(classification_report(y_test, y_pred))
print()
print('Tree depth:', model.get_depth())
print('Number of leaves:', model.get_n_leaves())
