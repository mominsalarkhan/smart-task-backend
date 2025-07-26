class PriorityModel:
    def __init__(self, model, vectorizer):
        self.model = model
        self.vectorizer = vectorizer

    def predict(self, texts):
        X = self.vectorizer.transform(texts)
        return self.model.predict(X)