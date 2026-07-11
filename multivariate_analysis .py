# ============================================
# Credit Card Approval Prediction
# Multivariate Analysis
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
app = pd.read_csv("data/application_record.csv")

# Select numerical columns
numeric_data = app.select_dtypes(include=['int64', 'float64'])

# Correlation Matrix
correlation = numeric_data.corr()

print("Correlation Matrix")
print(correlation)

# Heatmap
plt.figure(figsize=(10,8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# Pair Plot
selected_columns = ['AMT_INCOME_TOTAL', 'CNT_CHILDREN', 'DAYS_BIRTH', 'CNT_FAM_MEMBERS']
sns.pairplot(app[selected_columns])
plt.show()

# Box Plot
plt.figure(figsize=(8,5))
sns.boxplot(x='CODE_GENDER', y='AMT_INCOME_TOTAL', data=app)
plt.title("Income Distribution by Gender")
plt.show()
# Multivariate Analysis

## Description

Multivariate Analysis is performed to study the relationship between two or more variables in the dataset. It helps identify feature dependencies, correlations, and patterns that influence credit card approval.

## Objectives

- Analyze relationships among multiple features.
- Generate a correlation matrix.
- Visualize correlations using a heatmap.
- Explore feature interactions using pair plots.
- Compare numerical variables across categories using box plots.

## Methods Used

- corr()
- sns.heatmap()
- sns.pairplot()
- sns.boxplot()

## Features Analyzed

- Annual Income
- Number of Children
- Age (Days Birth)
- Family Members
- Gender

## Outcome

The multivariate analysis highlights relationships between important applicant attributes, helping in feature selection, reducing redundancy, and improving the machine learning model's performance.
