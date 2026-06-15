import pandas as pd

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, classification_report
except ImportError as e:
    raise ImportError(
        "Required package not installed. Install scikit-learn: pip install scikit-learn"
    ) from e

# Text analysis exercise with synthetic review data
reviews = [
    'I absolutely loved the product, it works perfectly.',
    'The service was terrible and I will not return.',
    'Great quality and fast shipping.',
    'This is a bad purchase, very disappointed.',
    'Excellent support and a quick response.',
    'I hate the experience, it was awful.',
    'The item is fine but shipping took too long.',
    'Very happy with the purchase and customer service.',
]
labels = ['positive', 'negative', 'positive', 'negative', 'positive', 'negative', 'negative', 'positive']

X_train, X_test, y_train, y_test = train_test_split(reviews, labels, test_size=0.25, random_state=42)

vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = LogisticRegression(max_iter=200)
model.fit(X_train_vec, y_train)
y_pred = model.predict(X_test_vec)

print('Text Analysis exercise')
print('Sample test reviews:')
for text, pred in zip(X_test, y_pred):
    print(f'- {text} => {pred}')
print()
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Classification report:')
print(classification_report(y_test, y_pred))
