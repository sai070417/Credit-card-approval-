# ============================================
# Credit Card Approval Prediction
# Read the Dataset
# ============================================

import pandas as pd

# Load datasets
application = pd.read_csv("data/application_record.csv")
credit = pd.read_csv("data/credit_record.csv")

# Display first 5 rows
print("Application Dataset")
print(application.head())

print("\nCredit Record Dataset")
print(credit.head())

# Display dataset shape
print("\nApplication Dataset Shape:", application.shape)
print("Credit Record Dataset Shape:", credit.shape)

# Display dataset information
print("\nApplication Dataset Info")
print(application.info())

print("\nCredit Record Dataset Info")
print(credit.info())

# Check missing values
print("\nMissing Values in Application Dataset")
print(application.isnull().sum())

print("\nMissing Values in Credit Dataset")
print(credit.isnull().sum())
# Read the Dataset

## Description

Reading the dataset is the first step after importing the required libraries. The datasets are loaded into Pandas DataFrames using the `pd.read_csv()` function. This allows us to inspect the data before preprocessing and model building.

## Files Used

- application_record.csv
- credit_record.csv

## Operations Performed

1. Load both CSV files.
2. Display the first five records using `head()`.
3. Check the number of rows and columns using `shape`.
4. View dataset information using `info()`.
5. Identify missing values using `isnull().sum()`.

## Expected Output

- Dataset preview
- Number of rows and columns
- Column names and data types
- Missing value summary

This step ensures that the dataset is correctly loaded and ready for exploratory data analysis and preprocessing.
