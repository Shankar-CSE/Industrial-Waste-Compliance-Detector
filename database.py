# ===========================
# database.py
# ===========================
from pymongo import MongoClient
from datetime import datetime

# Replace this with your actual MongoDB connection string
MONGO_URI = "mongodb://localhost:27017/"

# Initialize MongoDB client
client = MongoClient(MONGO_URI)
db = client["waste_compliance_db"]  # Database name
collection = db["predictions"]      # Collection name

def save_prediction(input_features, prediction, confidence, model_name):
    """
    Save prediction details to MongoDB Atlas.
    """
    record = {
        "timestamp": datetime.utcnow(),
        "input_features": input_features,
        "prediction": prediction,
        "confidence": confidence,
        "model_name": model_name
    }

    result = collection.insert_one(record)
    return result.inserted_id
