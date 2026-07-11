# ============================================
# Credit Card Approval Prediction
# Descriptive Analysis
# ============================================

import pandas as pd

# Load Dataset
app = pd.read_csv("data/application_record.csv")

# Display first 5 records
print("First 5 Records")
print(app.head())

# Dataset Shape
print("\nDataset Shape")
print(app.shape)

# Dataset Information
print("\nDataset Information")
print(app.info())

# Descriptive Statistics
print("\nDescriptive Statistics")
print(app.describe())

# Descriptive Statistics for Categorical Columns
print("\nCategorical Statistics")
print(app.describe(include='object'))

# Missing Values
print("\nMissing Values")
print(app.isnull().sum())

# Duplicate Records
print("\nDuplicate Records:", app.duplicated().sum())
