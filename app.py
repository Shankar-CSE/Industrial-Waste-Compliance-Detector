from flask import Flask, request, render_template
import numpy as np
import joblib

app = Flask(__name__)

# Load model and scaler
model = joblib.load('./models/stack_model.pkl')
scaler = joblib.load('./models/scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get values from form
    features = [float(x) for x in request.form.values()]
    final_features = np.array([features])  # make 2D

    # Scale input
    scaled_features = scaler.transform(final_features)

    # Predict
    prediction = model.predict(scaled_features)
    result = "positive" if prediction[0] == 1 else "negative"
    return render_template('index.html', prediction_text=f'Prediction: {result}')

if __name__ == "__main__":
    app.run()
