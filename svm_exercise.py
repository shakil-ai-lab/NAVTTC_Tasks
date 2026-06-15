import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Synthetic binary classification dataset for SVM
X, y = make_classification(
    n_samples=140,
    n_features=4,
    n_informative=3,
    n_redundant=0,
    n_clusters_per_class=1,
    class_sep=1.0,
    random_state=1
)

feature_names = [f'Feature_{i+1}' for i in range(X.shape[1])]
svm_df = pd.DataFrame(X, columns=feature_names)
svm_df['Target'] = y
print('SVM dataset sample:')
print(svm_df.head())
print()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
model = SVC(kernel='rbf', gamma='scale', probability=False)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print('SVM evaluation:')
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Classification Report:')
print(classification_report(y_test, y_pred))
