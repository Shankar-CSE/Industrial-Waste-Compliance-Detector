# data_preprocessing.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA

# ===============================
# STEP 1: Load the dataset
# ===============================
df = pd.read_csv("../data/raw_data.csv")

print("\n🔹 STEP 1: Dataset Loaded")
print("Shape:", df.shape)
print(df.head(5))  # show first 5 rows

# ===============================
# STEP 2: Handle Missing Values
# ===============================
print("\n🔹 STEP 2: Checking Missing Values")
print(df.isnull().sum())

# Visualize missing values
plt.figure(figsize=(10, 4))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values Heatmap")
plt.show()

# Fill missing values
num_cols = df.select_dtypes(include=[np.number]).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

cat_cols = df.select_dtypes(include=["object"]).columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("✅ Missing values handled")
print("Shape after filling NAs:", df.shape)

# ===============================
# STEP 3: Encode Categorical Columns
# ===============================
print("\n🔹 STEP 3: Encoding Categorical Columns")

encoder = LabelEncoder()
for col in cat_cols:
    df[col] = encoder.fit_transform(df[col])

print("✅ Categorical columns encoded")
print("Shape after encoding:", df.shape)

# ===============================
# STEP 4: Scale Numerical Features
# ===============================
print("\n🔹 STEP 4: Scaling Numerical Features")

scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

print("✅ Numerical features scaled")
print("Shape after scaling:", df.shape)

# Show histogram after scaling
df[num_cols].hist(bins=30, figsize=(12, 8))
plt.suptitle("Distribution of Numerical Features After Scaling")
plt.show()

# ===============================
# STEP 5: Apply PCA for Redundancy Reduction
# ===============================
print("\n🔹 STEP 5: Applying PCA for Dimensionality Reduction")

pca = PCA(n_components=0.95)  # keep 95% variance
pca_features = pca.fit_transform(df[num_cols])

# Variance explained plot
plt.figure(figsize=(8, 5))
plt.plot(np.cumsum(pca.explained_variance_ratio_), marker="o")
plt.xlabel("Number of Components")
plt.ylabel("Cumulative Explained Variance")
plt.title("PCA Explained Variance")
plt.grid()
plt.show()

# Replace numerical columns with PCA features
pca_cols = [f"PCA_{i+1}" for i in range(pca_features.shape[1])]
df_pca = pd.DataFrame(pca_features, columns=pca_cols)

df = df.drop(columns=num_cols).reset_index(drop=True)
df = pd.concat([df, df_pca], axis=1)

print("✅ PCA applied")
print("Shape after PCA:", df.shape)
print(df.head(5))

# ===============================
# STEP 6: Save Preprocessed Dataset
# ===============================
df.to_csv("../data/preprocessed_data.csv", index=False)
print("\n💾 Preprocessed dataset saved as 'preprocessed_data.csv'")

# ===============================
# STEP 7: Train-Test Split
# ===============================
print("\n🔹 STEP 7: Splitting into Train/Test Sets")

# Assuming last column is target (adjust as per your dataset)
x = df.iloc[:, :-1]
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

print("✅ Data split complete")
print("Train set shape:", X_train.shape, y_train.shape)
print("Test set shape:", X_test.shape, y_test.shape)