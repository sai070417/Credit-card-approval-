# ============================================
# Credit Card Approval Prediction
# Univariate Analysis
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
app = pd.read_csv("data/application_record.csv")

# Display basic statistics
print(app.describe(include='all'))

# Check occupation type frequency
print("\nOccupation Type Counts:")
print(app['OCCUPATION_TYPE'].value_counts())

# Plot Occupation Type
plt.figure(figsize=(12,6))
sns.countplot(
    x='OCCUPATION_TYPE',
    data=app,
    order=app['OCCUPATION_TYPE'].value_counts().index
)
plt.xticks(rotation=90)
plt.title("Occupation Type Distribution")
plt.tight_layout()
plt.show()

# Income Type Distribution
plt.figure(figsize=(8,5))
sns.countplot(x='NAME_INCOME_TYPE', data=app)
plt.xticks(rotation=45)
plt.title("Income Type Distribution")
plt.tight_layout()
plt.show()

# Gender Distribution
plt.figure(figsize=(5,4))
sns.countplot(x='CODE_GENDER', data=app)
plt.title("Gender Distribution")
plt.show()

# Annual Income Histogram
plt.figure(figsize=(8,5))
plt.hist(app['AMT_INCOME_TOTAL'], bins=30)
plt.title("Annual Income Distribution")
plt.xlabel("Annual Income")
plt.ylabel("Count")
plt.show()
# Univariate Analysis

## Description

Univariate Analysis is performed to study one feature at a time. It helps understand the distribution, frequency, and characteristics of each variable before model training.

## Objectives

- Analyze categorical features using count plots.
- Analyze numerical features using histograms.
- Detect missing values and outliers.
- Understand feature distributions.

## Methods Used

- value_counts()
- describe()
- sns.countplot()
- matplotlib histogram

## Features Analyzed

- Occupation Type
- Income Type
- Gender
- Annual Income

## Outcome

The analysis provides insights into the distribution of applicant characteristics, helping identify dominant categories, imbalanced data, and potential preprocessing requirements before building the machine learning model.
