from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app=Flask(__name__)
#Loading the model
with open("random_forest.pkl", "rb") as f:
    model=pickle.load(f)

@app.route("/")
def home():
    return "✅ House Price Predictor is running!"
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return jsonify({"predicted_price": float(prediction)})

if __name__ == "__main__":
    app.run(debug=True)

