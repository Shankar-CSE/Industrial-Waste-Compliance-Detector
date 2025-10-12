# STEP 1: Load & Inspect the Dataset

import pandas as pd

# 🧠 Load your dataset (make sure selected_features.csv is in the same folder)
df = pd.read_csv("./data/selected_features.csv")

# ✅ Basic Info
print("🔹 Dataset Loaded Successfully!")
print(f"📦 Shape: {df.shape[0]} rows × {df.shape[1]} columns\n")

# 🧾 Show column names
print("🔸 Columns in Dataset:")
# display(df.columns.tolist())

# 📊 Data types
print("\n🔸 Data Types:")
# display(df.dtypes)

# 👀 Preview first 5 rows
print("\n🔹 First 5 Rows of Data:")
# display(df.head())

# 🧩 Check for missing values
print("\n🔸 Missing Values per Column:")
# display(df.isnull().sum())


# STEP 2: Handle Missing Values

# 1️⃣ Separate numerical and categorical columns
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
cat_cols = df.select_dtypes(include=['object', 'bool']).columns

print("🔹 Numerical Columns:", num_cols.tolist())
print("🔸 Categorical Columns:", cat_cols.tolist())

# 2️⃣ Fill missing numerical values with median
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# 3️⃣ Fill missing categorical values with mode (most frequent) or 'Unknown'
for col in cat_cols:
    if df[col].isnull().sum() > 0:
        df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else "Unknown", inplace=True)

# 4️⃣ Check again for missing values
print("\n✅ Missing values after cleaning:")
# display(df.isnull().sum())

# 5️⃣ Optional: show confirmation
print("\n🎯 All missing values handled successfully!")


# STEP 3: Encode Categorical Variables

from sklearn.preprocessing import LabelEncoder

# display(df.head())


# 1️⃣ Identify categorical columns again
cat_cols = df.select_dtypes(include=['object', 'bool']).columns
print("🔸 Categorical Columns to Encode:")
# display(cat_cols)

# 2️⃣ Initialize label encoder
le = LabelEncoder()

# 3️⃣ Encode each categorical column
for col in cat_cols:
    df[col] = le.fit_transform(df[col].astype(str))

print("\n✅ Encoding completed successfully!")

# 4️⃣ Verify encoding result
print("\n🔹 Encoded Data Preview:")
# display(df.head())

# 5️⃣ Check data types after encoding
print("\n🔸 Data Types after Encoding:")
# display(df.dtypes)
print(df.shape)

df.to_csv("./data/cleaned_compliance_data.csv", index=False)


# STEP 4: Feature Scaling + PCA

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd

# 🧠 Separate target column before scaling
target_col = "Perfect_Waste_Decomposition_System"
X = df.drop(columns=[target_col])
y = df[target_col]

# 1️⃣ Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 1a️⃣ Save scaled features + target before PCA
df_scaled = pd.DataFrame(X_scaled, columns=X.columns)
df_scaled[target_col] = y.values
df_scaled.to_csv("./data/cleaned_compliance_data_scaled.csv", index=False)
print("✅ Scaled dataset saved: cleaned_compliance_data_scaled.csv")

# 2️⃣ Apply PCA - keep 95% variance
pca = PCA(n_components=0.95, random_state=42)
X_pca = pca.fit_transform(X_scaled)

# 3️⃣ Create a new DataFrame for PCA-transformed features
pca_columns = [f"PCA_{i+1}" for i in range(X_pca.shape[1])]
df_pca = pd.DataFrame(X_pca, columns=pca_columns)

# 4️⃣ Add back the target column
df_pca[target_col] = y.values

# 5️⃣ Save the PCA dataset
df_pca.to_csv("./data/cleaned_compliance_data_pca.csv", index=False)
print("✅ PCA dataset saved: cleaned_compliance_data_pca.csv")

# 6️⃣ Display summary
print(f"🔹 Original Features: {X.shape[1]}")
print(f"🔸 PCA Components Retained: {X_pca.shape[1]}")
# display(df_pca.head())
print(f"📦 Final PCA Dataset Shape: {df_pca.shape[0]} rows × {df_pca.shape[1]} columns")


import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
plt.bar(range(1, len(pca.explained_variance_ratio_)+1), pca.explained_variance_ratio_)
plt.plot(range(1, len(pca.explained_variance_ratio_)+1), pca.explained_variance_ratio_.cumsum(), color='red', marker='o')
plt.xlabel("PCA Component")
plt.ylabel("Variance Explained")
plt.title("PCA Explained Variance Ratio")
# plt.show()
