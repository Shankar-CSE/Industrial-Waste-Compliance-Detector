from flask import Flask, request, render_template
import numpy as np
import joblib
# from database import save_prediction 


# ===========================
#  Flask App Initialization
# ===========================
app = Flask(__name__)

# ===========================
#  Load Pre-trained Model and Scaler
# ===========================
# The model is a stacked ensemble (e.g., combining Random Forest, KNN, etc.)
# The scaler standardizes input features before prediction.
model = joblib.load('./models/stack_model.pkl')
scaler = joblib.load('./models/scaler.pkl')

@app.route('/')
def home():
    """
    Render the main HTML page.
    """
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """
    Handle prediction requests from the user via an HTML form.
    Steps:
    1. Collect and validate form data.
    2. Scale input features.
    3. Predict using the trained model.
    4. Return results and additional insights to the webpage.
    """
    try:
        # ===========================
        # Step 1: Get and validate inputs
        # ===========================
        input_values = list(request.form.values())
        features = [float(x) for x in input_values]  # Convert to float
        final_features = np.array([features])  # Convert to 2D array for model

        # ===========================
        # Step 2: Scale input features
        # ===========================
        scaled_features = scaler.transform(final_features)

        # ===========================
        # Step 3: Make predictions
        # ===========================
        prediction = model.predict(scaled_features)
        probabilities = getattr(model, "predict_proba", None)

        # Get class label (binary classification assumed: 0 = negative, 1 = positive)
        result_label = "Positive" if prediction[0] == 1 else "Negative"

        # Confidence score (if model supports probabilities)
        confidence = None
        if probabilities:
            confidence = model.predict_proba(scaled_features)[0][prediction[0]]
            confidence = round(confidence * 100, 2)  # Convert to percentage

        # ===========================
        # Step 4: Return the result
        # ===========================
        return render_template(
            'index.html',
            prediction_text=f"Prediction: {result_label}",
            confidence_text=f"Confidence: {confidence}%" if confidence else "Confidence: Not available",
            model_name="Stacked Ensemble Classifier",
            input_features=features
        )

    except ValueError:
        # Handle invalid inputs (like text in numeric fields)
        return render_template('index.html', prediction_text="❌ Invalid input! Please enter numeric values only.")

    except Exception as e:
        # Handle any other unexpected errors gracefully
        return render_template('index.html', prediction_text=f"⚠️ Error: {str(e)}")


if __name__ == "__main__":
    # ===========================
    #  Run the Flask app
    # ===========================
    # debug=True enables auto-reload and better error messages for development
    app.run(debug=True)
