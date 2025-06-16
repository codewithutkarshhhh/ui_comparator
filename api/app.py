from flask import Flask, request, render_template, jsonify
import joblib
import os

app = Flask(__name__)

@app.route("/")
def upload_form():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def handle_upload():
    f = request.files["file"]
    os.makedirs("uploads", exist_ok=True)
    f.save(os.path.join("uploads", f.filename))
    return f"Uploaded {f.filename}"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    model = joblib.load("analyzer/screen_classifier.pkl")
    features = [[data["feature1"], data["feature2"], data["feature3"]]]
    prediction = model.predict(features)
    return jsonify({"prediction": prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)

