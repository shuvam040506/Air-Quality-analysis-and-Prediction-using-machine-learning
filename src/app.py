from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__, template_folder='templates')
model = joblib.load('src/air_quality_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame(data)
    prediction = model.predict(df)
    return jsonify({"predictions": prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
