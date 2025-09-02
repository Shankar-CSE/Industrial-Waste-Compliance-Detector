# 🚀 ML Training Process

# 1. Load the Dataset
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import joblib





# Load dataset
df = pd.read_csv("data/waste_decomposition_dataset.csv")

# print(df.head())
# print(df.info())



# Target
y = df["Perfect_Waste_Decomposition_System"]

# Drop non-useful ID column
X = df.drop(["Company_ID", "Perfect_Waste_Decomposition_System"], axis=1)

# Encode categorical columns
categorical_cols = X.select_dtypes(include=["object"]).columns
encoder = LabelEncoder()

for col in categorical_cols:
    X[col] = encoder.fit_transform(X[col])

# print(X.head())


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)



# Train
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)



y_pred = model.predict(X_test)

# print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
# print("\nClassification Report:\n", classification_report(y_test, y_pred))




importances = model.feature_importances_
features = X.columns

# Sort and plot
indices = importances.argsort()[::-1]
plt.figure(figsize=(12,6))
plt.bar(range(len(features)), importances[indices])
plt.xticks(range(len(features)), features[indices], rotation=90)
plt.title("Feature Importance in Waste Decomposition Prediction")
# plt.show()

print("plot created")
import os

os.makedirs('model', exist_ok=True)
joblib.dump(model, "model/waste_decomposition_model.pkl")
print("✅ Model saved as waste_decomposition_model.pkl")