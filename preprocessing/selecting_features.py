import pandas as pd

# Step 1: Load the raw dataset
# 👉 Replace 'industrial_waste_data.csv' with your actual file name
df = pd.read_csv("./data/raw_data.csv")

# Step 2: Select the top 15 important columns
selected_columns = [
    "Waste_Segregation_Level_%",
    "Decomposition_Efficiency_%",
    "Recycling_Rate_%",
    "Hazardous_Waste_Treatment_Compliance",
    "Govt_Compliance_Status",
    "ISO_14001_Certified",
    "Zero_Waste_Landfill_Certified",
    "Waste_to_Energy_Usage",
    "CO2_Emissions_tons_per_year",
    "Methane_Emissions_tons_per_year",
    "Environmental_Fines_Count",
    "Employee_Training_in_Waste_Management",
    "Digital_Waste_Tracking",
    "Frequency_of_Waste_Audit_per_year",
    "Eco_Friendly_Raw_Materials_%",
    "Perfect_Waste_Decomposition_System"
]

# Step 3: Keep only those columns
df_selected = df[selected_columns]

# Step 4: Save the selected data into a new CSV file
df_selected.to_csv("./data/selected_features.csv", index=False)

print("✅ New dataset created successfully: selected_features.csv")
