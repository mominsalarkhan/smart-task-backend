import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load training data
texts = [
    "Submit project report tonight",
    "Buy groceries",
    "Pay electricity bill tomorrow",
    "Schedule team meeting next week",
    "Reply to urgent emails",
    "Start coding assignment",
]

labels = ["High", "Low", "Medium", "Low", "High", "Medium"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

# Predict function
def predict_priority(task):
    vec = vectorizer.transform([task])
    return model.predict(vec)[0]
