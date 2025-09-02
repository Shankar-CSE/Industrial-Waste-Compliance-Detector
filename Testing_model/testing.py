import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# 1. Load trained model
model = joblib.load("model/waste_decomposition_model.pkl")

# 2. Load test dataset (without target column)
df_test = pd.read_csv("data/waste_decomposition_without_target.csv")

# Keep original for saving later
df_original = df_test.copy()

# ---- IMPORTANT ----
# If you generated the dataset with label column originally, 
# but removed it for testing, keep that file separately as ground truth
try:
    y_true = pd.read_csv("data/waste_decomposition_with_target.csv")["Perfect_Waste_Decomposition_System"]
except:
    y_true = None  # If you don’t have labels, accuracy can’t be computed

# 3. Preprocess categorical columns
X_test = df_test.drop(["Company_ID"], axis=1)

categorical_cols = X_test.select_dtypes(include=["object"]).columns
encoder = LabelEncoder()

for col in categorical_cols:
    X_test[col] = encoder.fit_transform(X_test[col])

# 4. Predict
y_pred = model.predict(X_test)

import os

os.makedirs('data', exist_ok=True)

# 5. Save predictions to CSV
df_original["Predicted_Perfect_Waste_Decomposition_System"] = y_pred
df_original.to_csv("data/output.csv", index=False)

print("✅ Predictions saved to output.csv")

# 6. Accuracy if ground truth exists
if y_true is not None:
    acc = accuracy_score(y_true, y_pred)
    print("\n🎯 Testing Accuracy:", round(acc * 100, 2), "%")
else:
    print("⚠️ No ground truth labels available → accuracy cannot be calculated.")
