from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import os

app = Flask(__name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

INPUT_COLS = ["age", "bmi", "children", "smoker_code"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)

        age = float(data.get("age"))
        bmi = float(data.get("bmi"))
        children = int(data.get("children"))
        smoker = str(data.get("smoker", "")).strip().lower()

        if smoker not in ("yes", "no"):
            return jsonify({"error": "Smoker must be 'yes' or 'no'"}), 400
        if age <= 0 or age > 120:
            return jsonify({"error": "Enter a valid age"}), 400
        if bmi <= 0 or bmi > 80:
            return jsonify({"error": "Enter a valid BMI"}), 400
        if children < 0:
            return jsonify({"error": "Children cannot be negative"}), 400

        smoker_code = 1 if smoker == "yes" else 0

        row = pd.DataFrame(
            [[age, bmi, children, smoker_code]], columns=INPUT_COLS
        )
        prediction = model.predict(row)[0]
        prediction = max(0, round(float(prediction), 2))

        return jsonify({"prediction": prediction})

    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please check the values."}), 400
    except Exception as e:
        return jsonify({"error": "Something went wrong. Please try again."}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
