
import pandas as pd
import random
import numpy as np

# Number of records
num_records = 2000

# Possible categorical values
industry_types = ["Manufacturing", "Food", "Textile", "IT", "Pharma", "Construction", "Automobile"]
company_sizes = ["Small", "Medium", "Large"]
locations = ["Urban", "Rural", "Semi-Urban"]
decomposition_methods = ["Composting", "Anaerobic Digestion", "Incineration", "Recycling", "Landfill", "Mixed"]

data = []

for i in range(1, num_records + 1):
    company_id = f"C{i:04d}"
    industry = random.choice(industry_types)
    size = random.choice(company_sizes)
    location = random.choice(locations)

    # Waste data
    total_waste = round(random.uniform(500, 50000), 2)  # kg per month
    biodegradable_pct = random.randint(20, 70)
    recyclable_pct = random.randint(10, 50)
    hazardous_pct = max(0, 100 - (biodegradable_pct + recyclable_pct))
    segregation_level = random.randint(50, 100)

    # Treatment data
    method = random.choice(decomposition_methods)
    decomposition_eff = random.randint(60, 99)
    recycling_rate = random.randint(40, 95)
    hazardous_compliance = random.choice(["Yes", "No"])
    waste_to_energy = random.choice(["Yes", "No"])

    # Compliance
    iso_cert = random.choice(["Yes", "No"])
    zero_waste_cert = random.choice(["Yes", "No"])
    govt_status = random.choice(["Compliant", "Non-Compliant", "Pending"])
    fines = random.randint(0, 5)

    # Environmental impact
    co2 = round(random.uniform(50, 1000), 2)
    methane = round(random.uniform(10, 300), 2)
    water_pollution = random.randint(0, 100)
    soil_pollution = random.randint(0, 100)

    # Operational
    training = random.choice(["Yes", "No"])
    digital_tracking = random.choice(["Yes", "No"])
    audit_freq = random.randint(1, 12)
    eco_materials = random.randint(10, 90)

    # Community
    csr = random.choice(["Yes", "No"])
    sustainability_report = random.choice(["Yes", "No"])

    # Target: Perfect system (relaxed logic)
   # Target: Perfect system (much more relaxed logic)
    perfect_system = 1 if (
    segregation_level >= 70 and          # slightly easier
    decomposition_eff >= 70 and
    recycling_rate >= 60 and
    hazardous_compliance == "Yes" and
    govt_status in ["Compliant", "Pending"] and   # allow pending approvals too
    water_pollution <= 60 and             # higher threshold
    soil_pollution <= 60
    ) else 0


    data.append([
        company_id, industry, size, location,
        total_waste, biodegradable_pct, recyclable_pct, hazardous_pct, segregation_level,
        method, decomposition_eff, recycling_rate, hazardous_compliance, waste_to_energy,
        iso_cert, zero_waste_cert, govt_status, fines,
        co2, methane, water_pollution, soil_pollution,
        training, digital_tracking, audit_freq, eco_materials,
        csr, sustainability_report,
        perfect_system
    ])

# Define columns
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

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv("./data/raw_data.csv", index=False)

# Quick check of label distribution
print(df["Perfect_Waste_Decomposition_System"].value_counts())
print("✅ Dataset created: waste_decomposition_dataset.csv with", num_records, "records")