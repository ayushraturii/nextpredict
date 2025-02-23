from flask import Flask, render_template, request, jsonify
from predictor import load_trained_model, predict_next_word
import os

app = Flask(__name__)

# Load models for each style
models = {
    "casual": load_trained_model("models/casual_model.h5"),
    "formal": load_trained_model("models/formal_model.h5"),
    "technical": load_trained_model("models/technical_model.h5"),
    "email": load_trained_model("models/email_model.h5")
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_text = data.get("text", "")
    style = data.get("style", "casual")

    if style not in models:
        return jsonify({"error": "Invalid style selected"}), 400

    predictions = predict_next_word(style,models[style], input_text)

    return jsonify({"predictions": predictions})


def handler(event, context):
    return app(event, context)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port)
