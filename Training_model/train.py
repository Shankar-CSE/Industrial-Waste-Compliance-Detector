import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier, StackingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import joblib
import os
import seaborn as sns
import matplotlib.pyplot as plt

# Create models directory if it doesn't exist
os.makedirs("./models", exist_ok=True)

# -------------------------
# Load dataset
# -------------------------
df = pd.read_csv("./data/cleaned_compliance_data.csv")
target_col = "Perfect_Waste_Decomposition_System"
X = df.drop(columns=[target_col])
y = df[target_col]

# In train.py
feature_columns = X.columns.tolist()
joblib.dump(feature_columns, './models/feature_columns.pkl')

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

# -------------------------
# Scaling
# -------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save the scaler
joblib.dump(scaler, "./models/scaler.pkl")

# -------------------------
# Optional PCA (keep if needed)
# -------------------------
pca = PCA(n_components=0.95)  # Retain 95% variance
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)
joblib.dump(pca, "./models/pca.pkl")

# -------------------------
# Define base models for stacking
# -------------------------
base_models = [
    ('rf', RandomForestClassifier(n_estimators=100, random_state=42)),
    ('dt', DecisionTreeClassifier(random_state=42)),
    ('knn', KNeighborsClassifier(n_neighbors=5)),
    ('nb', GaussianNB())
]

# Meta-model
meta_model = LogisticRegression(max_iter=1000, random_state=42)

# Stacking classifier
stack_model = StackingClassifier(estimators=base_models, final_estimator=meta_model, cv=5, n_jobs=-1)

# -------------------------
# Train stacking model
# -------------------------
stack_model.fit(X_train_scaled, y_train)

# -------------------------
# Evaluate
# -------------------------
y_pred = stack_model.predict(X_test_scaled)
print("🏆 Stacking Model Performance (Scaled Data):")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, zero_division=0))

# Save the trained stacking model
joblib.dump(stack_model, "./models/stack_model.pkl")
print("✅ Stacking model saved at: ./models/stack_model.pkl")

# -------------------------
# Heatmap of base model predictions (optional)
# -------------------------
results = []
for name, model in base_models:
    model.fit(X_train_scaled, y_train)
    y_pred_base = model.predict(X_test_scaled)
    results.append({
        "Model": name,
        "Accuracy": accuracy_score(y_test, y_pred_base),
        "Precision": precision_score(y_test, y_pred_base, zero_division=0),
        "Recall": recall_score(y_test, y_pred_base, zero_division=0),
        "F1-Score": f1_score(y_test, y_pred_base, zero_division=0)
    })

results_df = pd.DataFrame(results).sort_values(by="F1-Score", ascending=False)

plt.figure(figsize=(10, 6))
sns.heatmap(results_df.set_index("Model"), annot=True, fmt=".2f", cmap="YlGnBu")
plt.title("Base Models Performance")
# plt.show()
