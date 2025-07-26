from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

# Load model
model = joblib.load("model.pkl")

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Smart Task Scheduler API is live!"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    task = data.get("task", "")
    priority = model.predict([task])[0]
    return jsonify({"predicted_priority": priority})

@app.route("/test", methods=["GET"])
def test():
    return jsonify({"task": task})

if __name__ == "__main__":
    app.run(debug=False)