from flask import Flask, request, render_template
import numpy as np
import joblib
from database import save_prediction   # ✅ Import MongoDB helper

# ===========================
#  Flask App Initialization
# ===========================
app = Flask(__name__)

# ===========================
#  Load Model and Scaler
# ===========================
model = joblib.load('./models/stack_model.pkl')
scaler = joblib.load('./models/scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Step 1: Get inputs
        input_values = list(request.form.values())
        features = [float(x) for x in input_values]
        final_features = np.array([features])

        # Step 2: Scale features
        scaled_features = scaler.transform(final_features)

        # Step 3: Predict
        prediction = model.predict(scaled_features)
        probabilities = getattr(model, "predict_proba", None)
        result_label = "Positive" if prediction[0] == 1 else "Negative"

        confidence = None
        if probabilities:
            confidence = model.predict_proba(scaled_features)[0][prediction[0]]
            confidence = round(confidence * 100, 2)

        # Step 4: Save to MongoDB ✅
        save_prediction(
            input_features=features,
            prediction=result_label,
            confidence=confidence,
            model_name="Stacked Ensemble Classifier"
        )

        # Step 5: Return to webpage
        return render_template(
            'index.html',
            prediction_text=f"Prediction: {result_label}",
            confidence_text=f"Confidence: {confidence}%" if confidence else "Confidence: Not available",
            model_name="Stacked Ensemble Classifier",
            input_features=features
        )

    except ValueError:
        return render_template('index.html', prediction_text="❌ Invalid input! Please enter numeric values only.")
    except Exception as e:
        return render_template('index.html', prediction_text=f"⚠️ Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
