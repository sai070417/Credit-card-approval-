# ============================================
# Credit Card Approval Prediction
# Handling Categorical Values
# ============================================

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("data/final_dataset.csv")

# Find categorical columns
categorical_columns = df.select_dtypes(include=['object']).columns

# Initialize LabelEncoder
encoder = LabelEncoder()

# Encode each categorical column
for column in categorical_columns:
    df[column] = encoder.fit_transform(df[column].astype(str))

# Display encoded dataset
print("Encoded Dataset Preview:")
print(df.head())

# Save encoded dataset
df.to_csv("data/encoded_dataset.csv", index=False)

print("\nCategorical values encoded successfully!")
