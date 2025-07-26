from sklearn.feature_extraction.text import CountVectorizer
from priority_model import PriorityModel
from sklearn.naive_bayes import MultinomialNB
import joblib

# Training data
X = [
    "submit assignment", "buy groceries", "call mom", "finish project",
    "watch netflix", "reply to emails", "urgent bug fix", "schedule dentist appointment"
]
y = ["High", "Low", "Low", "High", "Low", "High", "High", "Low"]

# Vectorization
vectorizer = CountVectorizer()
X_vect = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vect, y)

# Wrap with PriorityModel class (imported from priority_model.py)
wrapped_model = PriorityModel(model, vectorizer)

# Save to disk
joblib.dump(wrapped_model, "model.pkl")