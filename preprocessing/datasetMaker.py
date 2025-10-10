import pandas as pd
import random
import os
import numpy as np

# -------------------------
# Configuration
# -------------------------
num_records = 2000
half = num_records // 2

industry_types = ["Manufacturing", "Food", "Textile", "IT", "Pharma", "Construction", "Automobile"]
company_sizes = ["Small", "Medium", "Large"]
locations = ["Urban", "Rural", "Semi-Urban"]
decomposition_methods = ["Composting", "Anaerobic Digestion", "Incineration", "Recycling", "Landfill", "Mixed"]

# -------------------------
# Function to generate company
# -------------------------
def generate_company(is_perfect, i):
    company_id = f"C{i:04d}"
    industry = random.choice(industry_types)
    size = random.choice(company_sizes)
    location = random.choice(locations)

    # -------------------------
    # Numeric features with overlap
    # -------------------------
    # Overlapping ranges + Gaussian noise
    total_waste = round(random.uniform(2000, 40000), 2) + np.random.normal(0, 2000)
    biodegradable_pct = random.randint(20, 70)
    hazardous_pct = random.randint(0, 50)
    recyclable_pct = 100 - (biodegradable_pct + hazardous_pct)
    segregation_level = random.randint(30, 100)

    decomposition_eff = round(random.uniform(40, 99), 2)
    recycling_rate = round(random.uniform(10, 95), 2)
    co2 = round(random.uniform(50, 700) + np.random.normal(0, 50), 2)
    methane = round(random.uniform(10, 300) + np.random.normal(0, 20), 2)
    water_pollution = random.randint(0, 100)
    soil_pollution = random.randint(0, 100)

    method = random.choice(decomposition_methods)

    # -------------------------
    # Categorical features (probabilistic for perfect)
    # -------------------------
    def biased_choice(yes_prob):
        return "Yes" if random.random() < yes_prob else "No"

    hazardous_compliance = biased_choice(0.8 if is_perfect else 0.4)
    waste_to_energy = biased_choice(0.7 if is_perfect else 0.3)
    iso_cert = biased_choice(0.8 if is_perfect else 0.3)
    zero_waste_cert = biased_choice(0.75 if is_perfect else 0.3)
    govt_status = "Compliant" if is_perfect and random.random() < 0.75 else random.choice(["Non-Compliant", "Pending"])
    fines = 0 if is_perfect and random.random() < 0.7 else random.randint(1, 15)

    training = biased_choice(0.75 if is_perfect else 0.3)
    digital_tracking = biased_choice(0.75 if is_perfect else 0.3)
    audit_freq = random.randint(6, 12) if is_perfect else random.randint(0, 8)
    eco_materials = random.randint(50, 90) if is_perfect else random.randint(10, 70)
    csr = biased_choice(0.75 if is_perfect else 0.3)
    sustainability_report = biased_choice(0.75 if is_perfect else 0.3)

    # -------------------------
    # Target: probabilistic
    # -------------------------
    perfect_system = 1 if is_perfect and random.random() < 0.8 else 0

    return [
        company_id, industry, size, location,
        total_waste, biodegradable_pct, recyclable_pct, hazardous_pct, segregation_level,
        method, decomposition_eff, recycling_rate, hazardous_compliance, waste_to_energy,
        iso_cert, zero_waste_cert, govt_status, fines,
        co2, methane, water_pollution, soil_pollution,
        training, digital_tracking, audit_freq, eco_materials,
        csr, sustainability_report,
        perfect_system
    ]

# -------------------------
# Generate dataset
# -------------------------
data = []
for i in range(1, half + 1):
    data.append(generate_company(True, i))
for i in range(half + 1, num_records + 1):
    data.append(generate_company(False, i))

columns = [
    "Company_ID", "Industry_Type", "Company_Size", "Location_Region",
    "Total_Waste_Generated_kg_per_month", "Biodegradable_Waste_%", "Recyclable_Waste_%", "Hazardous_Waste_%", "Waste_Segregation_Level_%",
    "Decomposition_Technique", "Decomposition_Efficiency_%", "Recycling_Rate_%", "Hazardous_Waste_Treatment_Compliance", "Waste_to_Energy_Usage",
    "ISO_14001_Certified", "Zero_Waste_Landfill_Certified", "Govt_Compliance_Status", "Environmental_Fines_Count",
    "CO2_Emissions_tons_per_year", "Methane_Emissions_tons_per_year", "Water_Pollution_Index", "Soil_Pollution_Index",
    "Employee_Training_in_Waste_Management", "Digital_Waste_Tracking", "Frequency_of_Waste_Audit_per_year", "Eco_Friendly_Raw_Materials_%",
    "CSR_Initiatives_on_Waste", "Public_Sustainability_Reports",
    "Perfect_Waste_Decomposition_System"
]

df = pd.DataFrame(data, columns=columns)
df = df.sample(frac=1).reset_index(drop=True)

os.makedirs('./data', exist_ok=True)
df.to_csv("./data/raw_data.csv", index=False)
print("✅ Realistic noisy dataset saved at: ./data/raw_data.csv")
