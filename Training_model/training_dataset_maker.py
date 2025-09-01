import pandas as pd
import random

# Number of records
num_records = 2000
half = num_records // 2

industry_types = ["Manufacturing", "Food", "Textile", "IT", "Pharma", "Construction", "Automobile"]
company_sizes = ["Small", "Medium", "Large"]
locations = ["Urban", "Rural", "Semi-Urban"]
decomposition_methods = ["Composting", "Anaerobic Digestion", "Incineration", "Recycling", "Landfill", "Mixed"]

data = []

def generate_company(is_perfect, i):
    company_id = f"C{i:04d}"
    industry = random.choice(industry_types)
    size = random.choice(company_sizes)
    location = random.choice(locations)

    # Correlated waste data
    if size == "Large":
        total_waste = round(random.uniform(20000, 50000), 2)
    elif size == "Medium":
        total_waste = round(random.uniform(5000, 20000), 2)
    else:
        total_waste = round(random.uniform(500, 5000), 2)

    if industry == "Food":
        biodegradable_pct = random.randint(40, 70)
        hazardous_pct = random.randint(0, 20)
    elif industry == "Automobile":
        biodegradable_pct = random.randint(10, 30)
        hazardous_pct = random.randint(30, 60)
    else:
        biodegradable_pct = random.randint(20, 50)
        hazardous_pct = random.randint(10, 40)

    recyclable_pct = 100 - (biodegradable_pct + hazardous_pct)
    segregation_level = random.randint(60, 100) if is_perfect else random.randint(20, 70)

    # Treatment
    method = random.choice(decomposition_methods)
    decomposition_eff = random.randint(80, 99) if is_perfect else random.randint(40, 70)
    recycling_rate = random.randint(70, 95) if is_perfect else random.randint(10, 60)
    hazardous_compliance = "Yes" if is_perfect else random.choice(["Yes", "No"])
    waste_to_energy = "Yes" if is_perfect else random.choice(["Yes", "No"])

    # Compliance
    iso_cert = "Yes" if is_perfect else random.choice(["Yes", "No"])
    zero_waste_cert = "Yes" if is_perfect else random.choice(["Yes", "No"])
    govt_status = "Compliant" if is_perfect else random.choice(["Non-Compliant", "Pending"])
    fines = 0 if is_perfect else random.randint(1, 10)

    # Impact
    co2 = round(random.uniform(50, 200), 2) if is_perfect else round(random.uniform(300, 1000), 2)
    methane = round(random.uniform(10, 50), 2) if is_perfect else round(random.uniform(100, 300), 2)
    water_pollution = random.randint(0, 30) if is_perfect else random.randint(50, 100)
    soil_pollution = random.randint(0, 30) if is_perfect else random.randint(50, 100)

    # Ops
    training = "Yes" if is_perfect else random.choice(["Yes", "No"])
    digital_tracking = "Yes" if is_perfect else random.choice(["Yes", "No"])
    audit_freq = random.randint(6, 12) if is_perfect else random.randint(0, 5)
    eco_materials = random.randint(60, 90) if is_perfect else random.randint(10, 50)

    # Community
    csr = "Yes" if is_perfect else random.choice(["Yes", "No"])
    sustainability_report = "Yes" if is_perfect else random.choice(["Yes", "No"])

    perfect_system = 1 if is_perfect else 0

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


# Generate balanced dataset
for i in range(1, half + 1):
    data.append(generate_company(True, i))   # perfect
for i in range(half + 1, num_records + 1):
    data.append(generate_company(False, i))  # imperfect

# Shuffle
df = pd.DataFrame(data, columns=[
    "Company_ID", "Industry_Type", "Company_Size", "Location_Region",
    "Total_Waste_Generated_kg_per_month", "Biodegradable_Waste_%", "Recyclable_Waste_%", "Hazardous_Waste_%", "Waste_Segregation_Level_%",
    "Decomposition_Technique", "Decomposition_Efficiency_%", "Recycling_Rate_%", "Hazardous_Waste_Treatment_Compliance", "Waste_to_Energy_Usage",
    "ISO_14001_Certified", "Zero_Waste_Landfill_Certified", "Govt_Compliance_Status", "Environmental_Fines_Count",
    "CO2_Emissions_tons_per_year", "Methane_Emissions_tons_per_year", "Water_Pollution_Index", "Soil_Pollution_Index",
    "Employee_Training_in_Waste_Management", "Digital_Waste_Tracking", "Frequency_of_Waste_Audit_per_year", "Eco_Friendly_Raw_Materials_%",
    "CSR_Initiatives_on_Waste", "Public_Sustainability_Reports",
    "Perfect_Waste_Decomposition_System"
])

df = df.sample(frac=1).reset_index(drop=True)

# Save
df.to_csv("waste_decomposition_dataset.csv", index=False)

print(df["Perfect_Waste_Decomposition_System"].value_counts())
print("✅ Best dataset created with realistic balance and correlations")
