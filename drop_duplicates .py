# ============================================
# Credit Card Approval Prediction
# Drop Duplicate Records
# ============================================

import pandas as pd

# Load dataset
app = pd.read_csv("data/application_record.csv")

# Display original shape
print("Original Shape:", app.shape)

# Count duplicate rows
print("Duplicate Rows:", app.duplicated().sum())

# Remove duplicate rows
app = app.drop_duplicates()

# Display updated shape
print("Shape After Removing Duplicates:", app.shape)

# Save cleaned dataset
app.to_csv("data/application_record_clean.csv", index=False)

print("Duplicate records removed successfully!")
# Drop Duplicate Records

## Description

Removing duplicate records is an important preprocessing step in the Credit Card Approval Prediction project. Duplicate entries can occur due to repeated data collection, data merging, or system errors. These duplicate records may reduce the performance and accuracy of the machine learning model.

## Objectives

- Detect duplicate records in the dataset.
- Remove duplicate rows.
- Save the cleaned dataset for further preprocessing.

## Methods Used

- duplicated()
- drop_duplicates()
- to_csv()

## Output

- Original dataset size
- Number of duplicate records
- Cleaned dataset size
- Cleaned dataset saved as `application_record_clean.csv`

## Outcome

After removing duplicate records, the dataset becomes cleaner and more reliable, improving the quality of feature engineering, model training, and prediction.
