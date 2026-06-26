
# Fraud Message / Email Detector
# AI Club Summer Project 2026
# Model Training Scriptimport pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Read dataset
df = pd.read_csv(
    'data/SMSSpamCollection',
    sep='\t',
    names=['label', 'message']
)

# Convert labels
df['label'] = df['label'].map({'ham':0, 'spam':1})

# Features and labels
X = df['message']
y = df['label']

# Convert text into numbers
cv = CountVectorizer()
X = cv.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

import joblib

joblib.dump(model, "model.pkl")
joblib.dump(cv, "vectorizer.pkl")