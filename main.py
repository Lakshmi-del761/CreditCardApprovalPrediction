from flask import Flask, render_template, request, jsonify
from src.prediction import CreditCardApproval

app = Flask(__name__)

prediction = CreditCardApproval()

print(prediction.load_model())
print(prediction.load_encoders())
print(prediction.load_feature_names())


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    user_data = request.json

    result = prediction.predict(user_data)

    return jsonify({"prediction": result})


if __name__ == "__main__":
    app.run(debug=True)





