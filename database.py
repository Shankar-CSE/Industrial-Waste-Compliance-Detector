# ===========================
# database.py
# ===========================
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
