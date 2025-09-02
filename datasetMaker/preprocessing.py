import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load raw dataset
input_path = "data/raw_data.csv"
df = pd.read_csv(input_path)

# Step 1: Map Yes/No to 1/0 for binary columns
binary_columns = [
    "Hazardous_Waste_Treatment_Compliance", "Waste_to_Energy_Usage",
    "ISO_14001_Certified", "Zero_Waste_Landfill_Certified",
    "Employee_Training_in_Waste_Management", "Digital_Waste_Tracking",
    "CSR_Initiatives_on_Waste", "Public_Sustainability_Reports"
]

for col in binary_columns:
    df[col] = df[col].map({"Yes": 1, "No": 0})

# Step 2: Label Encode Categorical Columns
categorical_cols = [
    "Industry_Type", "Company_Size", "Location_Region",
    "Decomposition_Technique", "Govt_Compliance_Status"
]

label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le  # Save encoder if needed later

# Step 3: Scale Numeric Features (excluding target and already encoded columns)
target_col = "Perfect_Waste_Decomposition_System"

# Exclude non-numeric or already encoded/binary columns
exclude_cols = [target_col, "Company_ID"] + binary_columns + categorical_cols
numeric_cols = [col for col in df.columns if col not in exclude_cols and df[col].dtype in ['int64', 'float64']]



# Step 4: Save processed dataset
os.makedirs("data", exist_ok=True)
output_path = "data/processed_data.csv"
df.to_csv(output_path, index=False)

print("✅ Processed dataset saved to:", output_path)
