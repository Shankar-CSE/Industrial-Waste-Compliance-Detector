import pandas as pd
import random
import numpy as np

# Number of records
num_records = 200
half = num_records // 2  # 100 positive, 100 negative

industry_types = ["Manufacturing", "Food", "Textile", "IT", "Pharma", "Construction", "Automobile"]
company_sizes = ["Small", "Medium", "Large"]
locations = ["Urban", "Rural", "Semi-Urban"]
decomposition_methods = ["Composting", "Anaerobic Digestion", "Incineration", "Recycling", "Landfill", "Mixed"]

def generate_company(i, perfect=0):
    company_id = f"T{i:04d}"
    industry = random.choice(industry_types)
    size = random.choice(company_sizes)
    location = random.choice(locations)

    total_waste = round(random.uniform(500, 50000), 2)
    biodegradable_pct = random.randint(20, 70)
    recyclable_pct = random.randint(10, 50)
    hazardous_pct = max(0, 100 - (biodegradable_pct + recyclable_pct))
    segregation_level = random.randint(50, 100)

    method = random.choice(decomposition_methods)
    decomposition_eff = random.randint(60, 99)
    recycling_rate = random.randint(40, 95)
    hazardous_compliance = random.choice(["Yes", "No"])
    waste_to_energy = random.choice(["Yes", "No"])

    iso_cert = random.choice(["Yes", "No"])
    zero_waste_cert = random.choice(["Yes", "No"])
    govt_status = random.choice(["Compliant", "Non-Compliant", "Pending"])
    fines = random.randint(0, 5)

    co2 = round(random.uniform(50, 1000), 2)
    methane = round(random.uniform(10, 300), 2)
    water_pollution = random.randint(0, 100)
    soil_pollution = random.randint(0, 100)

    training = random.choice(["Yes", "No"])
    digital_tracking = random.choice(["Yes", "No"])
    audit_freq = random.randint(1, 12)
    eco_materials = random.randint(10, 90)

    csr = random.choice(["Yes", "No"])
    sustainability_report = random.choice(["Yes", "No"])

    # Force conditions for perfect system
    if perfect == 1:
        segregation_level = random.randint(80, 100)
        decomposition_eff = random.randint(85, 99)
        recycling_rate = random.randint(75, 95)
        hazardous_compliance = "Yes"
        govt_status = "Compliant"
        water_pollution = random.randint(0, 40)
        soil_pollution = random.randint(0, 40)

    # Force conditions for imperfect system
    else:
        segregation_level = random.randint(50, 79)
        decomposition_eff = random.randint(60, 79)
        recycling_rate = random.randint(40, 69)
        hazardous_compliance = random.choice(["No", "Yes"])
        govt_status = random.choice(["Non-Compliant", "Pending"])
        water_pollution = random.randint(41, 100)
        soil_pollution = random.randint(41, 100)

    return [
        company_id, industry, size, location,
        total_waste, biodegradable_pct, recyclable_pct, hazardous_pct, segregation_level,
        method, decomposition_eff, recycling_rate, hazardous_compliance, waste_to_energy,
        iso_cert, zero_waste_cert, govt_status, fines,
        co2, methane, water_pollution, soil_pollution, training,
        digital_tracking, audit_freq, eco_materials, csr,
        sustainability_report, perfect
    ]

# Generate data
data = []
for i in range(half):
    data.append(generate_company(i, perfect=1))  # 100 positives
for i in range(half, num_records):
    data.append(generate_company(i, perfect=0))  # 100 negatives

# Shuffle so it's not ordered
random.shuffle(data)

columns = [
    "Company_ID", "Industry_Type", "Company_Size", "Location_Region",
    "Total_Waste_Generated_kg_per_month", "Biodegradable_Waste_%", "Recyclable_Waste_%", "Hazardous_Waste_%", "Waste_Segregation_Level_%",
    "Decomposition_Technique", "Decomposition_Efficiency_%", "Recycling_Rate_%", "Hazardous_Waste_Treatment_Compliance", "Waste_to_Energy_Usage",
    "ISO_14001_Certified", "Zero_Waste_Landfill_Certified", "Govt_Compliance_Status", "Environmental_Fines_Count",
    "CO2_Emissions_tons_per_year", "Methane_Emissions_tons_per_year", "Water_Pollution_Index", "Soil_Pollution_Index",
    "Employee_Training_in_Waste_Management", "Digital_Waste_Tracking",
    "Frequency_of_Waste_Audit_per_year", "Eco_Friendly_Raw_Materials_%",
    "CSR_Initiatives_on_Waste", "Public_Sustainability_Reports",
    "Perfect_Waste_Decomposition_System"
]

df_with_target = pd.DataFrame(data, columns=columns)
import os

os.makedirs('data', exist_ok=True)
# Save the dataframe with the target column
df_with_target.to_csv("data/waste_decomposition_with_target.csv", index=False)
print(f"✅ Dataset with target column created: waste_decomposition_with_target.csv with {num_records} records")
print("Target column distribution:")
print(df_with_target["Perfect_Waste_Decomposition_System"].value_counts())
print("-" * 30)

# Create and save the dataframe without the target column
df_without_target = df_with_target.drop(columns=["Perfect_Waste_Decomposition_System"])
df_without_target.to_csv("data/waste_decomposition_without_target.csv", index=False)
print(f"✅ Dataset without target column created: waste_decomposition_without_target.csv with {num_records} records")
