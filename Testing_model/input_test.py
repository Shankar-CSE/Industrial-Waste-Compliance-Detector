import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

print("Load trained model...")

model = joblib.load("model/waste_decomposition_model.pkl")

print("Enter the following details to get prediction:")


company_id = input("Enter Company ID: ")
industry_type = input("Enter Industry Type: ")
company_size = input("Enter Company Size: ")
location_Region = input("Enter Location Region: ")
Total_waste_generated_per_year = float(input("Enter Total waste generated per year (in tons): "))
biodegradable_waste = int(input("Enter Biodegradable waste (in tons): "))
recyclable_waste = int(input("Enter Recyclable waste (in tons): "))
Hazardous_waste = int(input("Enter Hazardous waste (in tons): "))
waste_segregation_level = int(input("Enter Waste segregation level (1-100): "))
decomposition_technique = input("Enter Decomposition technique: ")
decomposition_efficiency = int(input("Enter Decomposition efficiency (1-100): "))
recycling_rate = int(input("Enter Recycling rate (1-100): "))
Hazardous_waste_treatment_compliance = input("Enter Hazardous waste treatment compliance (yes/no) : ")
waste_to_Energy_usage = input("Enter Waste to Energy usage (yes/no) : ")
iso_14001_certified = input("Is the company ISO 14001 certified? (Yes/No): ")
zero_waste_landfill_certified = input("Is the company Zero Waste to Landfill certified? (Yes/No): ")
govt_compliance_status = input("Enter Govt compliance status : ")
Environmental_fines_count = int(input("Enter Environmental fines count: "))
CO2_emissions_tons_per_year = float(input("Enter CO2 emissions (in tons per year): "))
Methane_emissions_tons_per_year = float(input("Enter Methane emissions (in tons per year): "))
water_polution_index = int(input("Enter Water pollution index: (i-100) "))
soil_pollution_index = int(input("Enter Soil pollution index:(1-100) "))
employee_training_in_waste_management = input("Enter Employee training in waste management (yes/no): ")
digital_waste_tracking = input("Enter Digital waste tracking (yes/no): ")
frequency_of_audits_per_year = int(input("Enter Frequency of audits per year:(1-20) "))
eco_friendly_raw_materials = int(input("Enter Eco-friendly raw materials (1-100): "))
CSR_initiatives_on_waste = input("Enter CSR initiatives on waste management (yes/no): ")
public_sustainability_reports = input("Enter Public sustainability reports (yes/no): ")



new_data = pd.DataFrame([[company_id, industry_type, company_size, location_Region, Total_waste_generated_per_year, biodegradable_waste, recyclable_waste, Hazardous_waste, waste_segregation_level, decomposition_technique, decomposition_efficiency, recycling_rate, Hazardous_waste_treatment_compliance, waste_to_Energy_usage, iso_14001_certified, zero_waste_landfill_certified, govt_compliance_status, Environmental_fines_count, CO2_emissions_tons_per_year, Methane_emissions_tons_per_year, water_polution_index, soil_pollution_index, employee_training_in_waste_management, digital_waste_tracking, frequency_of_audits_per_year, eco_friendly_raw_materials, CSR_initiatives_on_waste, public_sustainability_reports]],

columns=[
    "Company_ID", "Industry_Type", "Company_Size", "Location_Region",
    "Total_Waste_Generated_kg_per_month", "Biodegradable_Waste_%", "Recyclable_Waste_%", "Hazardous_Waste_%", "Waste_Segregation_Level_%",
    "Decomposition_Technique", "Decomposition_Efficiency_%", "Recycling_Rate_%", "Hazardous_Waste_Treatment_Compliance", "Waste_to_Energy_Usage",
    "ISO_14001_Certified", "Zero_Waste_Landfill_Certified", "Govt_Compliance_Status", "Environmental_Fines_Count",
    "CO2_Emissions_tons_per_year", "Methane_Emissions_tons_per_year", "Water_Pollution_Index", "Soil_Pollution_Index",
    "Employee_Training_in_Waste_Management", "Digital_Waste_Tracking", "Frequency_of_Waste_Audit_per_year", "Eco_Friendly_Raw_Materials_%",
    "CSR_Initiatives_on_Waste", "Public_Sustainability_Reports"
])

X_new = new_data.drop(["Company_ID"], axis=1)

categorical_cols = X_new.select_dtypes(include=["object"]).columns
encoder = LabelEncoder()

for col in categorical_cols:
    X_new[col] = encoder.fit_transform(X_new[col])

prediction = model.predict(X_new)

# print("Prediction:", prediction==0 if "No" else "Yes" )


if prediction[0] == 0:
    print("Prediction: Non-Compliant")
else:
    print("Prediction: Compliant")

