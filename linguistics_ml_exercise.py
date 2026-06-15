import pandas as pd

try:
    from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.pipeline import Pipeline
    from sklearn.metrics import accuracy_score, classification_report
except ImportError as e:
    raise ImportError(
        "Required package not installed. Install scikit-learn: pip install scikit-learn"
    ) from e

# Linguistics exercise using text processing and machine learning
texts = [
    "I love natural language processing and machine learning.",
    "Text classification is a great application of linguistics.",
    "This movie was amazing and I enjoyed it.",
    "The movie was boring and too long.",
    "Sentiment analysis can detect positive or negative emotion.",
    "I did not like the taste of this food.",
    "Language models can read and write human language.",
    "The plot was dull but the acting was decent.",
]
labels = ['topic', 'topic', 'positive', 'negative', 'topic', 'negative', 'topic', 'negative']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.25, random_state=42)

# Build a pipeline using TF-IDF and Naive Bayes
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', ngram_range=(1, 2))),
    ('clf', MultinomialNB()),
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

print('Text processing and linguistics ML exercise')
print('Test texts:')
print(X_test)
print()
print('Predicted labels:')
print(y_pred)
print()
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Classification report:')
print(classification_report(y_test, y_pred))
