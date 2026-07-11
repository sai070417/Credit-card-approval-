# ============================================
# Credit Card Approval Prediction
# Handling Missing Values
# ============================================

import pandas as pd

# Load dataset
app = pd.read_csv("data/application_record_clean.csv")

# Check missing values
print("Missing Values (Count):")
print(app.isnull().sum())

print("\nMissing Values (Percentage):")
print((app.isnull().mean() * 100).round(2))

# Fill missing numerical values with median
numeric_columns = app.select_dtypes(include=['int64', 'float64']).columns
app[numeric_columns] = app[numeric_columns].fillna(app[numeric_columns].median())

# Fill missing categorical values with mode
categorical_columns = app.select_dtypes(include=['object']).columns
for col in categorical_columns:
    app[col] = app[col].fillna(app[col].mode()[0])

# Verify missing values
print("\nMissing Values After Cleaning:")
print(app.isnull().sum())

# Save cleaned dataset
app.to_csv("data/application_record_missing_handled.csv", index=False)

print("\nMissing values handled successfully!")
