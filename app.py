from flask import Flask, request, render_template
import numpy as np
import joblib
from pymongo import MongoClient
from datetime import datetime
import os

# MongoDB connection string (use env variable for deployment safety)
MONGO_URI = "mongodb+srv://user:user@cluster0.8f5vc9l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Initialize MongoDB client
client = MongoClient(MONGO_URI)
db = client["waste_compliance_db"]        # Database name
predictions_collection = db["predictions"]  # Collection name

def save_prediction(input_features, prediction, confidence, model_name):
    """
    Save a prediction record to MongoDB Atlas.
    """
    record = {
        "timestamp": datetime.utcnow(),
        "input_features": input_features,
        "prediction": prediction,
        "confidence": confidence,
        "model_name": model_name
    }
    try:
        result = predictions_collection.insert_one(record)
        return result.inserted_id
    except Exception as e:
        print(f"⚠️ Failed to save to MongoDB: {e}")
        return None


app = Flask(__name__)

# Load model & scaler
model = joblib.load('./models/stack_model.pkl')
scaler = joblib.load('./models/scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/history')
def history():
    try:

        # MongoDB connection string (use env variable for deployment safety)
       

        # Fetch all prediction records from MongoDB (sorted by timestamp descending)
        records = list(predictions_collection.find().sort("timestamp", -1))
        # Convert datetime objects to string for easier display
        for r in records:
            r['timestamp'] = r['timestamp'].strftime("%Y-%m-%d %H:%M:%S")
        return render_template('history.html', records=records)
    except Exception as e:
        return f"⚠️ Error fetching history: {str(e)}"


@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_values = list(request.form.values())
        features = [float(x) for x in input_values]
        final_features = np.array([features])

        scaled_features = scaler.transform(final_features)

        prediction = model.predict(scaled_features)
        probabilities = getattr(model, "predict_proba", None)

        result_label = "Positive" if prediction[0] == 1 else "Negative"
        confidence = None
        if probabilities:
            confidence = model.predict_proba(scaled_features)[0][prediction[0]]
            confidence = round(confidence * 100, 2)

        # ✅ Save prediction to MongoDB
        save_prediction(
            input_features=features,
            prediction=result_label,
            confidence=confidence,
            model_name="Stacked Ensemble Classifier"
        )

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
