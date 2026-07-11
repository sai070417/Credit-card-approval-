# ============================================
# Credit Card Approval Prediction
# Data Cleaning and Feature Transformation
# ============================================

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load cleaned dataset
app = pd.read_csv("data/application_record_missing_handled.csv")

# Remove unwanted duplicate rows
app.drop_duplicates(inplace=True)

# Convert negative values to positive
if 'DAYS_BIRTH' in app.columns:
    app['DAYS_BIRTH'] = app['DAYS_BIRTH'].abs()

if 'DAYS_EMPLOYED' in app.columns:
    app['DAYS_EMPLOYED'] = app['DAYS_EMPLOYED'].abs()

# Create Total Family Members feature
if 'CNT_CHILDREN' in app.columns and 'CNT_FAM_MEMBERS' in app.columns:
    app['TOTAL_FAMILY_MEMBERS'] = (
        app['CNT_CHILDREN'] + app['CNT_FAM_MEMBERS']
    )

# Encode categorical columns
encoder = LabelEncoder()

for col in app.select_dtypes(include='object').columns:
    app[col] = encoder.fit_transform(app[col].astype(str))

# Save cleaned dataset
app.to_csv("data/application_record_final.csv", index=False)

print("Data cleaning and feature transformation completed successfully!")
